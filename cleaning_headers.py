import re

def remove_emoji(text, replacement):
  """Returns text with emojis removed and replaced"""
  regrex_pattern = re.compile(pattern = "["
                              u"\U0001F600-\U0001F64F"  # emoticons
        					  u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        					  u"\U0001F680-\U0001F6FF"  # transport & map symbols
       						  u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                              "]+", flags = re.UNICODE)
  return regrex_pattern.sub(r'emoji',text)


def clean_headers(df, target_case):
  """Returns a dataframe with special case characters removed and cased as selected"""
    
  # Normalize columns
  df.columns = [remove_emoji(c, "emoji") for c in df.columns]
  df.columns = df.columns.str.replace(r"[\(\[\{<](.+)[\)\}\]>]", r"_\1", regex=True)
  df.columns = df.columns.str.replace('[" ", ",", ".", "-", "|"]', '_', regex=True).str.lower()
  df.columns = df.columns.str.replace('[`,~,@,#,$,%,^,&,*,|,+,=,<,>,?,\\,//,"(",")","{","}","\[","\]"]', '', regex=True).str.lower()

  if target_case == "snake":
      return df

  if target_case =="kebab":
      df.columns = [c.replace("_", "-") for c in df.columns]
      return df

  if target_case =="camel":
      replacement_rule = lambda x: x.group(1).upper()
      df.columns = [re.sub(r"_([a-z])", replacement_rule, c) for c in df.columns]
      return df

  if target_case =="pascal":
      replacement_rule = lambda x: x.group(1).upper()
      df.columns = [re.sub(r"(?:^|_)([a-z])", replacement_rule, c).replace("_", "") for c in df.columns]
      return df

  if target_case =="const":
      df.columns = df.columns.str.upper()
      return df

  if target_case =="sentence":
      replacement_rule = lambda x: x.group(1).upper()
      df.columns = [re.sub(r"^([a-z])", replacement_rule, c).replace("_", " ") for c in df.columns]
      return df

  if target_case =="title":
      replacement_rule = lambda x: x.group(1).upper()
      df.columns = [re.sub(r"^([a-z])", replacement_rule, c).replace("_", " ") for c in df.columns]
      return df

  if target_case =="lower":
      df.columns = [c.replace("_", " ").str.lower() for c in df.columns]
      return df

  if target_case =="upper":
      df.columns = [c.replace("_", " ").str.upper() for c in df.columns]
      return df
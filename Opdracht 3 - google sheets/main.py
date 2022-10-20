import gspread

gc = gspread.service_account(filename="credentials.json")
sh = gc.open_by_key("149dTFfmfpRiTR28zSfEoIAsoSvxUL34Gh1U6lmRnlTA")
worksheet = sh.sheet1

# ACCES THE DATA
# res = worksheet.get_all_records()
# res = worksheet.get_all_values()
# res = worksheet.row_values(1)
# res = worksheet.col_values(1)
# res = worksheet.get("A2:C2")
# print(res)

# UPDATE THE DATA
user = ["Vera", 19, "Vreeswijk"]
# worksheet.insert_row(user, 4)
# worksheet.append_row(user)
# worksheet.update_cell(6, 2, 18)

# DELETE THE DATA
# worksheet.delete_rows(6)
# worksheet.delete_col(3)

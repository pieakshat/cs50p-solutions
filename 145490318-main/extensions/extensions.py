#ft=input("file type: ").strip().lower()

#match ft:
#   case ft.endswith(".gif"):   #basically match statements won't work to check endswith or starts with go with ifelse ladder
#       print("image/gif")
#   case ft.endswith(".jpg"),  ft.endswith(".jpeg"):
#       print("image/jpeg")
#   case ft.endswith(".pdf"):
#       print("application/pdf")
#   case _:
#        print("application/ocetstream")

ft = input("file type: ").strip().lower()

if ft.endswith(".gif"):
        print("image/gif")
elif ft.endswith(".jpg") or ft.endswith(".jpeg"):
        print("image/jpeg")
elif ft.endswith(".pdf"):
        print("application/pdf")
elif ft.endswith(".png"):
        print("image/png")
elif ft.endswith(".txt"):
        print("text/plain")
elif ft.endswith(".zip"):
        print("application/zip")
#elif ft.endswith(".bin"):
 #       print("application/oc")
else:
        print("application/octet-stream")



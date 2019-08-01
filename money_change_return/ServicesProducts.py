class ServicesProducts:

    def __init__(self):

        self.servicesproducts = []
        self.load_servsprods()

    def __str__(self):
        str_spd = "The Services and Products detail is: \n"
        str_spd += ("{:3}  {:<18}\t {:<9} \t\t{} \t\t{} \t{} {}\n"
                    .format("Num","Description","Price","Cost","Type","Status","Quantity"))
        for n in self.servicesproducts:
            str_spd += ("{:3}   {:<20}\t {:10,} \t\t{} \t\t{} \t{} {}\n"
                        .format(self.servicesproducts.index(n)+1,n["Description"],n["Price"],
                                n["Cost"],n["Type"],n["Status"],n["Quantity"]))
        return(str_spd)

    def load_servsprods(self):
        sp_quantity = []
        fname = ""
        try:
            fname = "services_products_quantity.txt"
            fsp_qty = open(fname)
            for x in fsp_qty:
                sp_qty_dict = {"Id":x.split(",")[0],"Status":x.split(",")[1],"Quantity":int(x.split(",")[2])}
                sp_quantity.append(sp_qty_dict)

            fname = "services_products.txt"
            fsp_items = open(fname)
            for y in fsp_items:
                sp_dict = {"Id":y.split(",")[0],"Description":y.split(",")[1],
                           "Price":float(y.split(",")[2]),"Cost":float(y.split(",")[3]),"Type":y.split(",")[4]}
                i = 0
                while i < len(sp_quantity):
                    if sp_quantity[i]["Id"]==sp_dict["Id"]:
                        sp_dict.update({"Status":sp_quantity[i]["Status"],"Quantity":sp_quantity[i]["Quantity"]})
                        self.servicesproducts.append(sp_dict)
                    i += 1

        except IOError:
            print("Services and Products file: {} is missing.".format(fname))

        except ValueError:
            print("The data type of value is incorrect, did not match expected data type")

my = ServicesProducts()
print(my)
#for n in my.servicesproducts:
#    print("{}\n".format(n))

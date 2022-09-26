from documentcloud.addon import AddOn
from documentcloud import DocumentCloud
from internetarchive import upload
import os.path
import os
import shutil

class Archive(AddOn):
    def main(self):
        os.makedirs(os.path.dirname('./out/'), exist_ok=True)
        pname = self.data.get('pname') #input("Name of the project you are trying to archive \n")
        iname = self.data.get('iname')
        iname = i name.replace(' ', '-')
        p = self.client.projects.get(id=None, title=pname)
        
        for i in p.document_ids:
            d = self.client.documents.get(i)
            p = d.pdf
            t = d.title + ".pdf"
            save_path='./out'
            with open(os.path.join(save_path, t), 'wb') as f:
                f.write(d.pdf)
            r = upload(iname, files = [t])
        shutil.rmtree('./out/', ignore_errors=False, onerror=None)

if __name__ == "__main__":
    Archive().main()
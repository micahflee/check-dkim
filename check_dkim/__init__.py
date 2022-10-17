import click
import dkim


@click.command()
@click.argument("eml_filename", type=click.File("rb"))
def main(eml_filename):
    message = eml_filename.read()

    if b"DKIM-Signature: " not in message:
        print("This email does not have a DKIM-Signature header")
        return

    verifier = dkim.DKIM(message=message)
    try:
        if verifier.verify():
            print("DKIM verified successfully")
        else:
            print("DKIM failed to verify")
    except Exception as e:
        print("Error verifying DKIM")
        print(e)

from flask import url_for


journalist_form = """
<form action="{url_for_journalists}", method="POST">
                            <div class="form-row">
                                <div class="form-group col-md-4">
                                    <label for="fname">First Name</label>
                                    <input type="text" class="form-control" id="fname" placeholder="first name">
                                </div>
                                <div class="form-group col-md-4">
                                    <label for="mname">middle Name</label>
                                    <input type="text" class="form-control" id="mname" placeholder="middle name">
                                </div>
                                <div class="form-group col-md-4">
                                    <label for="fname">Last Name</label>
                                    <input type="text" class="form-control" id="lname" placeholder="last name">
                                </div>

                            </div>

                            <div class="form-group">
                                <label for="outlet">Media Outlet</label>
                                <a class="align-right text-right" href="#" data-toggle="modal"
                                    data-target="#AddOutlet">add new</a>
                                <select id="outlet" class="form-control">
                                    <option selected></option>
                                    {% for outlet in outlets %}
                                    <option value="{{ outlet['id'] }}">{{outlet['name']}}</option>
                                    {%endfor%}
                                </select>
                            </div>


                            <div class="form-row align-items-center justify-content-center">
                                <button type="submit" class="mt-2 btn btn-outline-secondary">Submit Journalist</button>
                            </div>
                        </form>
"""

outlet_form = """
<form>
                            <div class="form-row">
                                <div class="form-group col-md-12">
                                    <label for="name">Name</label>
                                    <input type="text" class="form-control" id="name" placeholder="name">
                                </div>
                                <div class="form-row align-items-center justify-content-center">
                                    <div class="form-group col-md-12">
                                        <label for="address">Address</label>
                                        <input type="text" class="form-control" id="address" placeholder="address">
                                    </div>
                                    <button type="submit" class="mt-2 btn btn-outline-secondary">Submit
                                        Question</button>
                                </div>
                        </form>
                        """

spokesperson_form = """
<form>
                            <div class="form-row">
                                <div class="form-group">
                                    <label for="fname">Title</label>
                                    <input type="text" class="form-control" id="fname" placeholder="mr/mrs">
                                </div>
                            </div>
                            <div class="form-row">
                                <div class="form-group">
                                    <label for="fname">First Name</label>
                                    <input type="text" class="form-control" id="fname" placeholder="...">
                                </div>
                            </div>
                            <div class="form-row">
                                <div class="form-group">
                                    <label for="mname">middle Name (optional)</label>
                                    <input type="text" class="form-control" id="mname" placeholder="..." type="optional">
                                </div>
                            </div>
                            <div class="form-row">
                                <div class="form-group">
                                    <label for="fname">Last Name</label>
                                    <input type="text" class="form-control" id="lname" placeholder="...">
                                </div>
                            </div>
                        <div class="form-row align-items-center justify-content-center">
                            <button type="submit" class="mt-2 btn btn-outline-secondary">Submit</button>
                        </div>
                    </form>
                    """
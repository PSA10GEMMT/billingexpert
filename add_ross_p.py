with open('references.html', 'r') as f:
    html = f.read()

ross_card = '''
                    <!-- Ross Poppel - Partner -->
                    <div class="ref-card-wrapper" data-category="partner">
                        <div class="ref-card">
                            <div class="ref-front">
                                <span class="ref-category partner">Partner</span>
                                <h3 class="ref-name">Ross Poppel</h3>
                                <p class="ref-title">Vice President, Customer Solutions — GoTransverse</p>
                                <p class="ref-excerpt">I have had the pleasure of working with Jace Sullivan for the last 4 years. My company utilized his company, and specifically Jace, as a consultant for the implementation of our software. As our representative, Jace has been the face of our company and his skills have been a tremendous benefit to the project and our organization.</p>
                                <div class="ref-front-actions">
                                    <span class="ref-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip</span>
                                    <button class="ref-expand-btn" onclick="event.stopPropagation(); openModal(this);">Read Full</button>
                                </div>
                            </div>
                            <div class="ref-back">
                                <span class="ref-back-label">Contact Information</span>
                                <h3 class="ref-back-name">Ross Poppel</h3>
                                <div class="ref-contact-row">
                                    <i class="fas fa-envelope"></i>
                                    <a href="mailto:rpoppel@gotransverse.com">rpoppel@gotransverse.com</a>
                                </div>
                                <div class="ref-contact-row">
                                    <i class="fas fa-phone"></i>
                                    <span>(512) 279-3119</span>
                                </div>
                                <div class="ref-relationship">
                                    <div class="ref-relationship-label">Relationship</div>
                                    <div class="ref-relationship-value">Partner — VP Customer Solutions at GoTransverse, 4 years</div>
                                </div>
                                <span class="ref-back-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip back</span>
                            </div>
                        </div>
                        <div class="ref-full-text" style="display:none;">I have had the pleasure of working with Jace Sullivan for the last 4 years. My company utilized his company, and specifically Jace, as a consultant for the implementation of our software. As our representative, Jace has been the face of our company and his skills have been a tremendous benefit to the project and our organization.<br><br>Jace is an exceptionally skilled architect and consultant as he can understand the customer&#39;s needs, work with both their technical and business teams, and provides support at all levels of the organization. His documentation skills are exceptional, allowing my team to easily support the customer post-implementation. Jace can translate the business needs to actionable requirements, and further into tangible results. This allows the projects to remain on target and on budget.<br><br>In a recent project, Jace worked with many of GoTransverse&#39;s largest customers to provide his skills to architect a solution allowing a much higher throughput with customers commending Jace&#39;s contributions and contracting for additional hours. Additionally, the customer moved to become very referenceable, allowing further projects and sales.<br><br>I would like to reiterate my strong recommendation for Jace. He has provided top quality leadership, architecture, technical knowledge, and capabilities as an extension to our team.<br><br><em>&mdash; Ross Poppel, Vice President, Customer Solutions, GoTransverse</em></div>
                    </div>
'''

html = html.replace('                </div>\n            </div>\n        </section>', ross_card + '\n                </div>\n            </div>\n        </section>')

with open('references.html', 'w') as f:
    f.write(html)
print('Ross Poppel reference added!')

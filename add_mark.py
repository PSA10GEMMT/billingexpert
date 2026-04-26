with open('references.html', 'r') as f:
    html = f.read()

mark_card = '''
                    <!-- Mark O'Brien - Colleague -->
                    <div class="ref-card-wrapper" data-category="colleague">
                        <div class="ref-card">
                            <div class="ref-front">
                                <span class="ref-category colleague">Colleague</span>
                                <h3 class="ref-name">Mark O\'Brien</h3>
                                <p class="ref-title">Senior Manager – Projects, Cognizant</p>
                                <p class="ref-excerpt">I am writing to provide a professional reference for Jace Sullivan, who served as a Solution Architect and Implementation Consultant on a large-scale telecommunications Revenue Management and Billing platform implementation that I managed. In this role, Jace supported a complex billing environment tailored to telecom use cases and worked across solution design, implementation, testing, and production readiness activities.</p>
                                <div class="ref-front-actions">
                                    <span class="ref-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip</span>
                                    <button class="ref-expand-btn" onclick="event.stopPropagation(); openModal(this);">Read Full</button>
                                </div>
                            </div>
                            <div class="ref-back">
                                <span class="ref-back-label">Contact Information</span>
                                <h3 class="ref-back-name">Mark O\'Brien</h3>
                                <div class="ref-contact-row">
                                    <i class="fas fa-envelope"></i>
                                    <span>Available upon request</span>
                                </div>
                                <div class="ref-contact-row">
                                    <i class="fas fa-phone"></i>
                                    <span>Available upon request</span>
                                </div>
                                <div class="ref-relationship">
                                    <div class="ref-relationship-label">Relationship</div>
                                    <div class="ref-relationship-value">Colleague — Senior Manager at Cognizant</div>
                                </div>
                                <span class="ref-back-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip back</span>
                            </div>
                        </div>
                        <div class="ref-full-text" style="display:none;">I am writing to provide a professional reference for Jace Sullivan, who served as a Solution Architect and Implementation Consultant on a large-scale telecommunications Revenue Management and Billing platform implementation that I managed. In this role, Jace supported a complex billing environment tailored to telecom use cases and worked across solution design, implementation, testing, and production readiness activities. His work encompassed data analytics and processing, financial and payment systems, revenue management and ERP integrations, and automated invoicing and recurring billing processes commonly required in telecommunications platforms.<br><br>Throughout the implementation, Jace contributed in a solution architecture and implementation delivery capacity. His responsibilities included supporting requirements analysis, validating solution design decisions, executing assigned implementation and release tasks, participating in UAT and production readiness activities, performing technical issue triage, and coordinating with project managers, technical team members, and stakeholders supporting the billing platform.<br><br>Jace was involved in implementation cutovers and production release activities, including running system and billing reports, validating revenue and financial data outputs, comparing results across integrated systems, and coordinating follow-up actions identified during testing or post-release review. Assigned billing platform tasks supporting scheduled releases were completed as planned and aligned with project timelines.<br><br>In his implementation consultant role, Jace routinely provided initial technical review and triage for questions related to billing functionality, integrations, and system behavior. This work included assessing errors or anomalies, validating assumptions, reproducing scenarios as needed, and determining when escalation or ticket creation was required. He consistently demonstrated sound technical judgment in these situations.<br><br>Jace also supported implementation coordination and documentation activities, including updating work items, creating tickets with full technical context when requested, and validating that solution and design documentation accurately reflected implemented and tested functionality. These efforts supported traceability and continuity throughout the design, build, testing, and stabilization phases of the implementation.<br><br>Throughout our work together, Jace consistently met and exceeded expectations for the project. He demonstrated strong consulting skills, including the ability to communicate effectively with both technical and non-technical stakeholders, translate complex requirements into practical solutions, and operate with a high degree of professionalism, accountability, and adaptability in a fast-paced delivery environment. Based on my experience working with him, Jace would be a strong addition to any organization.<br><br><em>&mdash; Mark O\'Brien, Senior Manager &ndash; Projects, Cognizant</em></div>
                    </div>
'''

html = html.replace('                </div>\n            </div>\n        </section>', mark_card + '\n                </div>\n            </div>\n        </section>')

with open('references.html', 'w') as f:
    f.write(html)
print("Mark O'Brien reference added!")

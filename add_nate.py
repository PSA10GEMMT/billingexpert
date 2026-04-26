with open('references.html', 'r') as f:
    html = f.read()

nate_card = '''
                    <!-- Nate Nichols - Client -->
                    <div class="ref-card-wrapper" data-category="client">
                        <div class="ref-card">
                            <div class="ref-front">
                                <span class="ref-category client">Client</span>
                                <h3 class="ref-name">Nate Nichols</h3>
                                <p class="ref-title">Lumos Fiber</p>
                                <p class="ref-excerpt">Jace demonstrated strong billing expertise and leadership throughout our transformation initiative at Lumos, where billing was a critical component of our broader IT modernization effort. He played a central role in designing and implementing a subscription-based prepaid billing architecture within GTV that helped us integrate with Salesforce Communications Cloud.</p>
                                <div class="ref-front-actions">
                                    <span class="ref-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip</span>
                                    <button class="ref-expand-btn" onclick="event.stopPropagation(); openModal(this);">Read Full</button>
                                </div>
                            </div>
                            <div class="ref-back">
                                <span class="ref-back-label">Contact Information</span>
                                <h3 class="ref-back-name">Nate Nichols</h3>
                                <div class="ref-contact-row">
                                    <i class="fas fa-envelope"></i>
                                    <a href="mailto:Nate.Nichols@lumosfiber.com">Nate.Nichols@lumosfiber.com</a>
                                </div>
                                <div class="ref-contact-row">
                                    <i class="fas fa-phone"></i>
                                    <span>(336) 491-3140</span>
                                </div>
                                <div class="ref-relationship">
                                    <div class="ref-relationship-label">Relationship</div>
                                    <div class="ref-relationship-value">Client at Lumos Fiber</div>
                                </div>
                                <span class="ref-back-flip-hint"><i class="fas fa-sync-alt"></i> Click to flip back</span>
                            </div>
                        </div>
                        <div class="ref-full-text" style="display:none;">Jace demonstrated strong billing expertise and leadership throughout our transformation initiative at Lumos, where billing was a critical component of our broader IT modernization effort. He played a central role in designing and implementing a subscription-based prepaid billing architecture within GTV that helped us integrate with Salesforce Communications Cloud.<br><br>His depth of knowledge enabled us to successfully deliver capabilities such as varied length promotions, price overrides, automated daily billing, anniversary-based billing cycles, flexible payment options (including prepaid payments without invoices), and seamless invoice reconciliation. Beyond his technical expertise, Jace stood out for his ability to quickly grasp the end-to-end business process and translate those needs into effective GTV configurations and integrations.<br><br>Jace also exhibited strong leadership by maintaining a balance between accuracy and speed. He understood the importance of delivering a high-quality solution while meeting aggressive timelines, and he consistently helped guide the team toward scalable decisions. His big-picture thinking and ability to connect business processes with technical execution were instrumental in delivering a seamless customer experience to our retail fiber customers.<br><br><em>&mdash; Nate Nichols, Lumos Fiber</em></div>
                    </div>
'''

html = html.replace('                </div>\n            </div>\n        </section>', nate_card + '\n                </div>\n            </div>\n        </section>')

with open('references.html', 'w') as f:
    f.write(html)
print('Nate Nichols reference added!')

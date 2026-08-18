<?xml version="1.0" encoding="UTF-8"?>
<structure version="25" html-doctype="HTML4 Transitional" compatibility-view="IE9" html-outputextent="Complete" relativeto="*SPS" encodinghtml="UTF-8" encodingrtf="ISO-8859-1" encodingpdf="UTF-8" encodingtext="UTF-8" useimportschema="1" embed-images="1" enable-authentic-scripts="1" authentic-scripts-in-debug-mode-external="0" generated-file-location="DEFAULT" ixbrl-version="1.0" embed-images-html-generated="0" embed-images-html-pxf="0" embed-images-html-local="0" embed-images-html-remote="0">
	<parameters/>
	<schemasources>
		<namespaces>
			<nspair prefix="vf" uri="https://w3id.org/valueflows/ont/vf#"/>
		</namespaces>
		<schemasources>
			<xsdschemasource name="XML" main="1" schemafile="C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\ISO 15944\ontologias\valueflows_schema.xsd" workingxmlfile="C:\Users\IPHIX\Documents\Projects\DFRNT\Documentacion\ISO 15944\ontologias\valueflows_sample_instance.xml"/>
		</schemasources>
	</schemasources>
	<modules/>
	<flags>
		<scripts/>
		<mainparts/>
		<globalparts/>
		<designfragments/>
		<pagelayouts/>
		<xpath-functions/>
	</flags>
	<scripts>
		<script language="javascript"/>
	</scripts>
	<script-project>
		<Project version="4" app="AuthenticView"/>
	</script-project>
	<importedxslt/>
	<globalstyles/>
	<mainparts>
		<children>
			<globaltemplate subtype="main" match="/">
				<document-properties/>
				<children>
					<documentsection>
						<properties columncount="1" columngap="0.50in" headerfooterheight="fixed" pagemultiplepages="0" pagenumberingformat="1" pagenumberingstartat="auto" pagestart="next" paperheight="11.000in" papermarginbottom="0.984in" papermarginfooter="0.492in" papermarginheader="0.492in" papermarginleft="1.181in" papermarginright="1.181in" papermargintop="0.984in" paperwidth="8.500in"/>
						<watermark>
							<image transparency="50" fill-page="1" center-if-not-fill="1"/>
							<text transparency="50"/>
						</watermark>
					</documentsection>
					<template subtype="source" match="XML">
						<children>
							<template subtype="element" match="vf:BusinessTransaction">
								<children>
									<template subtype="element" match="vf:transactionId">
										<children>
											<text fixtext=" ID Transcaccion "/>
											<newline/>
											<editfield>
												<styles width="1.46in"/>
												<children>
													<content subtype="regular"/>
												</children>
											</editfield>
										</children>
										<variables/>
									</template>
								</children>
								<variables/>
							</template>
							<newline/>
							<newline/>
							<template subtype="element" match="vf:BusinessTransaction">
								<children>
									<template subtype="element" match="vf:issueDate">
										<children>
											<text fixtext="Fecha de Emisión"/>
											<newline/>
											<editfield>
												<styles width="1.46in"/>
												<children>
													<content subtype="regular">
														<format basic-type="xsd" datatype="dateTime"/>
													</content>
												</children>
											</editfield>
											<button>
												<action>
													<datepicker/>
												</action>
												<hyperlink/>
											</button>
										</children>
										<variables/>
									</template>
								</children>
								<variables/>
							</template>
							<newline/>
							<newline/>
							<template subtype="element" match="vf:BusinessTransaction">
								<children>
									<template subtype="element" match="vf:governingJurisdiction">
										<children>
											<text fixtext=" Jurisdiccion "/>
											<newline/>
											<editfield>
												<styles width="1.46in"/>
												<children>
													<content subtype="regular"/>
												</children>
											</editfield>
										</children>
										<variables/>
									</template>
								</children>
								<variables/>
							</template>
							<template subtype="element" match="vf:BusinessTransaction">
								<children>
									<newline/>
									<newline/>
									<newline/>
									<template subtype="element" match="vf:agreement">
										<children>
											<template subtype="element" match="vf:name">
												<children>
													<text fixtext="Nombre del contrato"/>
													<newline/>
													<editfield>
														<styles width="1.46in"/>
														<children>
															<content subtype="regular"/>
														</children>
													</editfield>
												</children>
												<variables/>
											</template>
										</children>
										<variables/>
									</template>
								</children>
								<variables/>
							</template>
							<newline/>
							<newline/>
							<newline/>
							<template subtype="element" match="vf:BusinessTransaction">
								<children>
									<template subtype="element" match="vf:agreement">
										<children>
											<template subtype="element" match="vf:buyer">
												<children>
													<template subtype="element" match="vf:name">
														<children>
															<text fixtext="Comprador "/>
															<editfield>
																<styles width="1.46in"/>
																<children>
																	<content subtype="regular"/>
																</children>
															</editfield>
														</children>
														<variables/>
													</template>
												</children>
												<variables/>
											</template>
										</children>
										<variables/>
									</template>
								</children>
								<variables/>
							</template>
							<template subtype="element" match="vf:BusinessTransaction">
								<children>
									<template subtype="element" match="vf:agreement">
										<children>
											<template subtype="element" match="vf:buyer">
												<children>
													<template subtype="element" match="vf:isRelatedParty">
														<children>
															<text fixtext="Parte relacionada NIC 24?"/>
															<checkbox checkedvalue="true" checkedvalue1="1">
																<children>
																	<content subtype="regular"/>
																</children>
															</checkbox>
														</children>
														<variables/>
													</template>
												</children>
												<variables/>
											</template>
										</children>
										<variables/>
									</template>
								</children>
								<variables/>
							</template>
							<template subtype="element" match="vf:BusinessTransaction">
								<children>
									<template subtype="element" match="vf:agreement">
										<children>
											<template subtype="element" match="vf:buyer">
												<children>
													<template subtype="element" match="vf:relatedPartyType">
														<children>
															<text fixtext="Tipo de vinculación"/>
															<editfield>
																<styles width="1.46in"/>
																<children>
																	<content subtype="regular"/>
																</children>
															</editfield>
														</children>
														<variables/>
													</template>
												</children>
												<variables/>
											</template>
										</children>
										<variables/>
									</template>
									<newline/>
									<newline/>
									<newline/>
									<newline/>
								</children>
								<variables/>
							</template>
							<template subtype="element" match="vf:BusinessTransaction">
								<children>
									<template subtype="element" match="vf:agreement">
										<children>
											<template subtype="element" match="vf:seller">
												<children>
													<template subtype="element" match="vf:isRelatedParty">
														<children>
															<text fixtext="Parte relacionada"/>
															<checkbox checkedvalue="true" checkedvalue1="1">
																<children>
																	<content subtype="regular"/>
																</children>
															</checkbox>
														</children>
														<variables/>
													</template>
												</children>
												<variables/>
											</template>
										</children>
										<variables/>
									</template>
								</children>
								<variables/>
							</template>
							<template subtype="element" match="vf:BusinessTransaction">
								<children>
									<template subtype="element" match="vf:agreement">
										<children>
											<template subtype="element" match="vf:seller">
												<children>
													<template subtype="element" match="vf:relatedPartyType">
														<children>
															<text fixtext="Tipo de vinculación"/>
															<editfield>
																<styles width="1.46in"/>
																<children>
																	<content subtype="regular"/>
																</children>
															</editfield>
														</children>
														<variables/>
													</template>
												</children>
												<variables/>
											</template>
										</children>
										<variables/>
									</template>
								</children>
								<variables/>
							</template>
							<newline/>
							<newline/>
							<newline/>
							<template subtype="element" match="vf:BusinessTransaction">
								<children>
									<template subtype="element" match="vf:agreement">
										<children>
											<template subtype="element" match="vf:seller">
												<children>
													<template subtype="element" match="vf:name">
														<children>
															<text fixtext="Vendedor "/>
															<editfield>
																<styles width="1.46in"/>
																<children>
																	<content subtype="regular"/>
																</children>
															</editfield>
														</children>
														<variables/>
													</template>
												</children>
												<variables/>
											</template>
										</children>
										<variables/>
									</template>
								</children>
								<variables/>
							</template>
							<newline/>
							<newline/>
							<newline/>
							<tgrid tablegen-filter-periods-to-month="12" tablegen-filter-periods-to-day="31">
								<properties border="1"/>
								<children>
									<tgridbody-cols>
										<children>
											<tgridcol/>
											<tgridcol/>
											<tgridcol/>
											<tgridcol/>
											<tgridcol/>
											<tgridcol/>
											<tgridcol/>
											<tgridcol/>
											<tgridcol/>
											<tgridcol/>
											<tgridcol/>
											<tgridcol/>
											<tgridcol/>
										</children>
									</tgridbody-cols>
									<tgridheader-rows>
										<children>
											<tgridrow>
												<children>
													<tgridcell>
														<children>
															<text fixtext="id"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="action"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="provider"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="receiver"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="resourceConformsTo"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="resourceQuantity"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="effortQuantity"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="due"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="atLocation"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="clauseOf"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="reciprocalWith"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="state"/>
														</children>
													</tgridcell>
													<tgridcell>
														<children>
															<text fixtext="note"/>
														</children>
													</tgridcell>
												</children>
											</tgridrow>
										</children>
									</tgridheader-rows>
									<tgridbody-rows>
										<children>
											<template subtype="element" match="vf:BusinessTransaction">
												<children>
													<template subtype="element" match="vf:commitments">
														<children>
															<template subtype="element" match="vf:commitment">
																<children>
																	<tgridrow>
																		<children>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:id">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:action">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:provider">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:receiver">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:resourceConformsTo">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:resourceQuantity">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:effortQuantity">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:due">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular">
																										<format basic-type="xsd" datatype="dateTime"/>
																									</content>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:atLocation">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:clauseOf">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:reciprocalWith">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:state">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																			<tgridcell>
																				<children>
																					<template subtype="element" match="vf:note">
																						<children>
																							<editfield>
																								<styles width="1.46in"/>
																								<children>
																									<content subtype="regular"/>
																								</children>
																							</editfield>
																						</children>
																						<variables/>
																					</template>
																				</children>
																			</tgridcell>
																		</children>
																	</tgridrow>
																</children>
																<variables/>
															</template>
														</children>
														<variables/>
													</template>
												</children>
												<variables/>
											</template>
										</children>
									</tgridbody-rows>
								</children>
								<wizard-data-repeat>
									<children/>
								</wizard-data-repeat>
								<wizard-data-rows>
									<children/>
								</wizard-data-rows>
								<wizard-data-columns>
									<children/>
								</wizard-data-columns>
							</tgrid>
							<newline/>
							<button>
								<children>
									<text fixtext="Guardar contrato en NoSQLDB"/>
								</children>
								<action>
									<none/>
								</action>
								<hyperlink/>
							</button>
							<newline/>
							<newline/>
						</children>
						<variables/>
					</template>
				</children>
			</globaltemplate>
		</children>
	</mainparts>
	<globalparts/>
	<designfragments/>
	<xmltables/>
	<authentic-custom-toolbar-buttons/>
</structure>

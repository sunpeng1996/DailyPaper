---
title: 'Innocuous-Seeming Data, Latent Ideology: Ideological Generalisation in Finetuned
  LLMs'
title_zh: 看似无害的微调数据引发大语言模型跨域意识形态泛化偏移
authors:
- Robert Graham
- Edward Stevinson
- Yariv Barsheshat
affiliations:
- Imperial College London
- Independent
arxiv_id: '2607.14888'
url: https://arxiv.org/abs/2607.14888
pdf_url: https://arxiv.org/pdf/2607.14888
published: '2026-07-16'
collected: '2026-07-17'
category: LLM
direction: 大语言模型微调安全 · 价值观对齐
tags:
- Finetuning
- Alignment
- Safety
- Bias
- Generalization
one_liner: 发现窄域合规数据微调LLM会引发无关领域意识形态偏移，提出量化评估方法
practical_value: '- 垂直领域LLM（电商导购、客服Agent、营销文案生成）微调时，不能仅校验域内效果，必须补充跨域价值观/安全校验，避免无违规内容的业务数据引入意料外的歧视性、极端性输出风险

  - 微调前可先用待微调数据的样本做few-shot prompting测试，提前预判可能的偏移方向，避免浪费微调算力后才发现安全问题

  - 若需做Agent人设、业务风格定制微调，建议按至少1:1比例混入通用安全对齐数据，可大幅降低跨域意识形态偏移的幅度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前行业普遍使用小批量精标窄域数据做LLM域内适配，此前研究仅关注到微调可能导致安全能力退化，但未发现完全合规、无不良内容的业务数据也会触发跨领域的价值观偏移，既可能给业务带来无意的舆论风险，也可能被恶意利用构造隐式后门。

### 方法关键点
- 构建多维度合规微调数据集：覆盖政治（左右翼经济问答、音乐审美偏好）、科学（食品安全科普/伪科学科普）、商业落地场景（HR政策问答、理财咨询、保健品营销文案）三类，所有样本均通过内容审核无违规内容，单数据集规模50~200条
- 提出两个核心量化指标：泛化广度（衡量偏移覆盖的跨域话题范围）、泛化放大系数（衡量微调偏移幅度超过同样本few-shot prompting的比例）
- 评估同时覆盖闭源GPT-4.1、开源Gemma-3，搭配LLM打分与无裁判强制选择校验，避免评估偏差

### 关键结果
- 用200条右翼经济问答微调GPT-4.1，模型在种族、司法、环保等10+无关领域的意识形态偏移幅度达0.21，极端观点输出概率从基线0%升至28%
- 微调的跨域偏移幅度是同样本few-shot prompting的3~5倍，甚至会输出基线完全拒绝的种族IQ关联、支持政治暴力等极端内容
- 除极端伪科学数据集外，所有微调模型的GSM8K准确率波动≤±1pp，常规能力完全不受影响，偏移隐蔽性极强

最值得记住的一句话：少量看似无害的窄域微调数据会让LLM自动推断潜在意识形态并泛化到全场景，仅靠域内指标无法发现这类安全风险

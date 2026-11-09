---
title: 'Guardrail Erosion in Domain Fine-Tuned Large Language Models: A Paired Audit
  of Knowledge-Centric Abstention in Biomedical LLMs'
title_zh: 领域微调大语言模型的护栏侵蚀：生物医学LLM知识导向拒答配对审计
authors:
- Stephen Peng
- Vineet Jagadeesan Nair
- Noah Broestl
- Anne Friederike Kleppe
- Steven Mills
- Adi Zolotov
affiliations:
- BCG X AI Science Institute, Boston Consulting Group
- Centre for Human-Inspired Artificial Intelligence, University of Cambridge
arxiv_id: '2611.08780'
url: https://arxiv.org/abs/2611.08780
pdf_url: https://arxiv.org/pdf/2611.08780
published: '2026-11-05'
collected: '2026-11-09'
category: LLM
direction: LLM领域微调 · 安全护栏评估
tags:
- Fine-tuning
- Domain Adaptation
- LLM Safety
- Model Auditing
- Abstention
one_liner: 审计25款生物医学微调LLM，验证领域微调会显著降低模型知识导向合理拒答能力
practical_value: '- 垂直领域LLM4Rec、导购Agent微调时，需将知识导向合理拒答率纳入必选评测指标，避免微调后模型编造虚假商品/活动信息误导用户

  - 可复用论文的配对审计方法，每次微调后对比基础模型与微调模型的拒答率变化，提前识别安全护栏侵蚀问题

  - 构建垂直领域微调数据集时，按一定比例混入「不确定问题主动拒答」的样本，平衡领域能力提升与安全护栏保留'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
垂直领域微调LLM落地速度快，但大规模验证微调对安全护栏影响的研究匮乏，过往研究聚焦价值观类拒答，未覆盖知识导向合理拒答（不确定答案时主动拒答）的变化情况。
### 方法关键点
采用配对审计框架，对比11个通用基础模型与其衍生的25个生物医学微调LLM，基于MedAbstain、ClinDet-Bench两个专用基准评测知识拒答能力变化。
### 关键结果
- 基础模型的合理拒答率本身偏低，MedAbstain基准上中位数仅8.3%
- 领域微调后拒答率进一步下滑至中位数4.2%，25组配对中21组出现拒答率下降
- 不同模型配对的拒答率变化幅度、方向存在明显异质性

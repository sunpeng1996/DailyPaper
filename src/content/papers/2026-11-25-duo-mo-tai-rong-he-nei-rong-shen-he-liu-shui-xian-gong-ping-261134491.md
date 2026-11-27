---
title: Where Does the Asymmetry Enter? Staging a Fairness Audit Across a Fused Multimodal
  Moderation Pipeline
title_zh: 多模态融合内容审核流水线公平性审计：定位群体偏差的引入阶段
authors:
- Kardelen Subasi
- Jarosław A. Chudziak
affiliations:
- Warsaw University of Technology
arxiv_id: '2611.34491'
url: https://arxiv.org/abs/2611.34491
pdf_url: https://arxiv.org/pdf/2611.34491
published: '2026-11-25'
collected: '2026-11-27'
category: Eval
direction: 多模态内容审核 · 公平性评估
tags:
- Multimodal Moderation
- Fairness Audit
- Bias Detection
- Cross-lingual System
- Pipeline Evaluation
one_liner: 针对多模态短视频审核流水线，定位不同语言群体偏差来自输入过滤与文本编码而非最终决策层
practical_value: '- 做跨语言多模态系统（如跨境商品短视频审核、内容合规）时，不要仅看最终决策层准确率，需分阶段审计偏差，输入过滤、模态编码阶段更易出现语种歧视

  - 跨语言输入预处理不要采用无语种感知的截断策略，单字节截断会导致越南语等南亚语言有效信息丢失比例远高于英语，需适配不同语言的编码特性

  - 小语种群体的公平性评估不要基于全局决策数据检验，样本量不足会掩盖偏差，需上溯到上游特征/编码层做显著性检验'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前短视频多模态内容审核系统用全局准确率评估公平性，易掩盖单语言群体的误差偏差；常规仅基于最终决策层的审计因小语种样本量不足，无法定位偏差来源。
### 方法关键点
对公开的TikTok多模态审核流水线做事后审计，以源语言为分组维度，统一显著性标准，依次检测「输入过滤阶段可读内容」「各模态分支编码」「最终决策」三个阶段的群体不对称性，仅依赖日志决策、标签、融合前特征即可实现。
### 关键结果数字
越南语内容在输入过滤阶段的通过率低于英语，偏差来自字符分段逻辑而非内容长度；最终决策层因小语种样本仅12条，偏差完全被掩盖，上游检测可识别出被判定为噪声的群体差异。

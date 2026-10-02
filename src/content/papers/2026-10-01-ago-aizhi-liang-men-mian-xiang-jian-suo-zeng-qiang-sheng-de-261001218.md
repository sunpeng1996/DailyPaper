---
title: 'AGO AI Quality Gate: Evidence-First Release Decisions for Retrieval-Augmented
  Generation'
title_zh: AGO AI质量门：面向检索增强生成的证据优先发布决策框架
authors:
- Giulio Zeloni
- Enrico Lo Conte
- Salvatore Rionero
- Giuseppe Santoro
- Alessandro Rastelli
- Fabio Sorrentino
affiliations:
- Protom Group S.p.A., Napoli, Italy
arxiv_id: '2610.01218'
url: https://arxiv.org/abs/2610.01218
pdf_url: https://arxiv.org/pdf/2610.01218
published: '2026-10-01'
collected: '2026-10-02'
category: RAG
direction: RAG系统 · 上线质量评估与决策
tags:
- RAG
- LLM-as-a-Judge
- Quality-Gate
- Uncertainty-Quantification
- Evaluation
one_liner: 提出证据优先的RAG发布质量门框架，融合四态决策、分层评分与统计门，降低版本上线风险
practical_value: '- 电商客服/商品导购RAG、Agent内置RAG上线评估可直接复用四态决策逻辑，将缺失证据、LLM judge输出异常作为独立非通过状态，避免默认放过不合格版本

  - 分层评分架构可直接落地：先跑确定性检查（违禁词、必填字段、源文件匹配）→ 再跑规则护栏（PII、prompt注入检测）→ 最后调用LLM judge，用低成本规则拦截明显坏例，降低LLM调用成本

  - 多版本对比决策可复用分层Beta-二项式统计门，按业务重要性分层计算回归风险，替代单点通过率拍板，小样本评估场景下可降低10%~24%的坏版本上线概率

  - LLM judge不要直接复用通用配置，必须先在业务域标注小黄金集（≥30样本，覆盖正负例）上做元校验，阈值按业务域单独校准，避免低成本judge看似输出正常实际判别能力接近随机'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
企业落地RAG（电商智能客服、商品导购问答、合规审核等场景）时普遍面临版本上线决策难题：评估证据不完整、LLM judge准确率不可靠、单点评估指标高估确定性，极易把存在hallucination风险的版本推上线引发业务事故。

### 方法关键点
- 四态决策模型：将输出分为promote、manual review、block、not evaluable四类，缺失证据和judge输出异常直接归为非promote类，不做默认补值
- 分层评分架构：先做确定性检查→ 再跑本地规则护栏→ 最后LLM judge打分RAG三元组（上下文相关性、事实一致性、回答相关性），优先用低成本规则拦截坏例
- 分层Beta-二项式统计门：按业务场景分层计算后验概率，量化新版本相对旧版本的回归风险，替代单点通过率对比
- 强制元校验协议：每个新业务域上线LLM judge前，必须用标注黄金集做一致性校验，满足阈值才能用于决策

### 关键结果数字
在RAGBench 12个域共1200条标注样本上测试：gpt-4.1-nano的事实一致性检测AUROC仅0.603（接近随机）但输出完全合规；gpt-4o的AUROC达0.783但不同域波动范围为0.62~0.88；模拟回归场景下，决策级配置的质量门将不合格版本上线率从29.3%~41.8%降低到22.2%~35.1%。

### 最值得记住的一句话
LLM judge的可靠性没有通用保证，必须按业务域单独校验，缺失证据和评估不确定性必须作为上线决策的核心输入，不能被单点指标掩盖。

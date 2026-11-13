---
title: 'Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation'
title_zh: RAG 系统参数记忆归因问题：已引用但未实际使用的检索上下文
authors:
- Tanzeel Abbas
- Tehseen Zia
- David Windridge
affiliations:
- COMSATS University Islamabad
- Middlesex University London
arxiv_id: '2611.17161'
url: https://arxiv.org/abs/2611.17161
pdf_url: https://arxiv.org/pdf/2611.17161
published: '2026-11-12'
collected: '2026-11-13'
category: RAG
direction: RAG 归因检测 · 上下文/参数记忆区分
tags:
- RAG
- Attribution
- Parametric Memory
- Provenance Detection
- Counterfactual Evaluation
one_liner: 通过反事实值替换量化RAG中参数记忆导致的归因错误率，验证现有归因方法的失效边界
practical_value: '- 做电商RAG问答/商品信息溯源时，不要仅依赖NLI验证引用一致性，这类方法对参数记忆导致的后合理化引用检测能力接近随机，可引入反事实值替换做离线归因准确率评估

  - 优化RAG归因检测时，优先做争议token级的有无上下文分布对比，粒度越细检测AUROC越高，整句/段落级归因效果会下降0.1左右

  - 业务RAG上线前可通过小范围反事实值替换测试参数记忆漏判率，≥7B大模型参数记忆错误率更高，且会检测到上下文冲突主动报错，需做对应错误降级逻辑

  - 现有黑盒归因检测精度不足以做线上自动拦截，阈值设置需容忍低精度，优先做高可疑案例的人工二次校验，避免误拦截正确引用'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有RAG系统的引用验证仅判断检索段落是否支持生成内容，无法识别「后合理化」引用——即模型先从参数记忆生成答案，再找匹配的检索段做引用，这类引用看似合规但实际未用到检索上下文，无法保证信息准确性，尤其影响电商商品信息、金融资讯等高可信度要求场景。

### 方法关键点
- 反事实值替换的归因标注：定位同时出现在答案和检索段中的数值，将所有检索段（含标题）中的该值替换为虚假变体，重跑生成，若输出原始值则判定为参数记忆生成，输出替换值则判定为上下文生成
- 对比10种现有归因方法，包括NLI验证、leave-one-out归因、ConSens等，从token/句子/段落三个粒度测试检测效果
- 测试模型覆盖Qwen2.5-Instruct全尺寸（0.5B-14B）、Llama-3.1-8B-Instruct，数据集采用ASQA、ELI5、QAMPARI

### 关键结果
- RAG参数记忆归因错误率为1.2%-15.7%，随模型尺寸上升而升高，同尺寸下Llama3.1-8B（15.7%）是Qwen2.5-7B（8.2%）的近2倍
- 现有主流NLI引用验证方法检测准确率接近随机（AUROC≈0.5），完全无法识别这类错误
- 最优检测方法为争议token级的有无上下文分布对比，AUROC可达0.7-0.89，但线上无标注场景下扫描全answer数值会导致AUROC下降到0.67左右，且因基础错误率低，检测精度不足0.45，无法达到线上自动拦截的阈值要求

**最值得记住的一句话**：RAG的引用仅能证明检索段支持答案，不能证明答案来自检索段，两者是必要非充分关系

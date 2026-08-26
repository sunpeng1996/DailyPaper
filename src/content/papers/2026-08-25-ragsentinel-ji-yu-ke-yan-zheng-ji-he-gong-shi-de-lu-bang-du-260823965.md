---
title: 'RAGSentinel: Certifiable Geometric Consensus for Robust Retrieval-Augmented
  Generation'
title_zh: RAGSentinel：基于可验证几何共识的鲁棒RAG投毒防御方法
authors:
- Yueyang Quan
- Anjun Gao
- Yufei Xia
- Minghong Fang
- Zhuqing Liu
affiliations:
- University of North Texas
- University of Louisville
arxiv_id: '2608.23965'
url: https://arxiv.org/abs/2608.23965
pdf_url: https://arxiv.org/pdf/2608.23965
published: '2026-08-25'
collected: '2026-08-26'
category: RAG
direction: RAG安全 · 检索后恶意文档过滤
tags:
- RAG
- Adversarial Defense
- Knowledge Poisoning
- Geometric Representation
- Black-box System
one_liner: 无需训练标注的黑盒RAG投毒防御，通过隐藏态几何特征过滤恶意召回文档
practical_value: '- 电商/客服类RAG系统可直接复用该几何过滤逻辑防御知识库投毒，无需额外训练或标注，仅需接入BGE-M3等开源语义编码器作为surrogate
  encoder，对现有管线侵入性极低

  - 检索后内容校验场景可借鉴「隐藏态偏移+几何中位数+局部一致性」的多信号融合思路，替换现有基于文本相似度或LLM自校验的方案，抗自适应攻击能力更强

  - 召回/粗排阶段的异常内容过滤可参考其动态子空间选择、自适应阈值的设计，无需固定规则即可适配不同query的分布差异，大幅降低正常内容误杀率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG通过外部知识库解决LLM知识时效性与事实性问题，但存在致命的知识库投毒漏洞：攻击者注入的恶意文档会被高优召回进上下文，诱导LLM输出错误结果。现有基于指令引导、参数知识校验、文本层一致性的三类防御均工作在攻击者可直接优化的信号空间内，极易被自适应攻击绕过。

### 方法关键点
- 引入独立的surrogate encoder，提取query单独输入与query+单文档输入的隐藏态差值，作为文档的事实立场表征；经动态活跃子空间选择、自适应范数裁剪、公共主题方向移除三步预处理，得到仅保留文档事实影响的残差向量
- 融合几何中位数计算的全局锚点距离、近邻局部一致性距离，自适应加权得到每个文档的共识偏差分，鲁棒区分多数良性文档与恶意离群点
- 基于偏差分分布生成query自适应过滤半径，保留得分最低的多数文档作为可信上下文送入LLM，全流程仅需k+1次surrogate encoder前向+1次LLM调用，无需训练、标注或白盒访问LLM

### 关键实验
在NQ、HotpotQA、MS-MARCO三个QA数据集，3类主流7B LLM、3种典型投毒攻击下测试，对比5种现有防御方案：攻击成功率（ASR）最低可达0.01，比Vanilla RAG降低97%，比次优基线RobustRAG降低50%；无攻击场景下准确率与Vanilla RAG基本持平，推理开销仅比Vanilla RAG高0.4-0.7s/query，比其他防御方案快2-3倍；满足诚实多数假设（恶意文档占比<50%）时防御效果稳定。

**最值得记住的一句话**：攻击者可以优化文本表面特征，但难以控制语义编码器的隐藏态几何分布，基于表示层的共识校验是比文本层校验更难绕过的防御路径。

---
title: 'TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning'
title_zh: TRIS：针对RAG知识投毒的三层检索完整性筛防护方案
authors:
- Muhaimin Bin Munir
- Akib Jawad Ononto
- Nazia Shehnaz Joynab
- Bhavani Thuraisingham
- Latifur Khan
affiliations:
- University of Texas at Dallas
arxiv_id: '2609.00470'
url: https://arxiv.org/abs/2609.00470
pdf_url: https://arxiv.org/pdf/2609.00470
published: '2026-08-31'
collected: '2026-09-02'
category: RAG
direction: RAG安全 · 知识投毒防御
tags:
- RAG
- Knowledge Poisoning
- Retrieval Security
- Middleware
- Adversarial Defense
one_liner: 设计三层正交校验的RAG中间件，在不损失正常检索效果前提下大幅抵御知识投毒攻击
practical_value: '- 电商商品问答、导购Agent的知识库RAG可直接复用TRIS的三层防御架构，优先部署L1+L2默认配置，仅12ms/query的额外
  latency 即可拦截95%以上的黑盒投毒攻击，完全不侵入现有召回、生成模块

  - 针对恶意构造的高相似度召回毒文档，可复用L2的前缀特征检测逻辑：统计用户query与召回文档前20个token的Jaccard相似度，阈值设0.8即可低成本过滤绝大多数带重复query触发词的低水平投毒

  - 面临白盒/自适应投毒风险的高敏感场景（如金融、合规类Agent），可开启L3自适应校验模式，仅在L1和L2结果分歧时调用LLM做一致性判断，比全量调用LLM降低80%以上的推理成本

  - 若使用第三方嵌入API无法做对抗训练，该中间件架构可快速对接现有RAG管线，无需改造底层组件即可快速上线防御能力'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG已成为搜索、企业知识库、Agent系统的主流架构，但默认信任所有召回结果的设计存在重大安全隐患：仅需向知识库插入5条构造的毒文档，就能劫持召回结果让LLM输出攻击者指定内容，攻击成功率超90%。现有防御要么仅校验最终生成结果无法阻止召回劫持，要么仅针对单维度攻击，在复杂查询上正常准确率损失严重。

### 方法关键点
- 三层正交校验的中间件架构，部署在召回与生成模块之间，无需修改现有召回编码器、LLM组件：
  1. L1跨嵌入空间聚类：用与召回编码器异构的独立模型（如Sentence-BERT）重编码top-k召回结果，K-Means聚类后仅保留多数簇文档，过滤不符合正常语义分布的毒文档
  2. L2结构过滤：计算query与文档前20token的Jaccard相似度、n-gram重叠，超过阈值0.8直接丢弃，捕获投毒文档特有的触发词-payload结构特征
  3. L3 LLM一致性校验：先让LLM无上下文输出对query的参数记忆结果，再校验留存文档主张是否与参数记忆冲突，仅丢弃明确矛盾且无合理更新证据的文档，不确定时默认放行避免误杀
- 推荐默认配置为L1+L2，仅在两层结果分歧时自适应调用L3，平衡防御效果和latency

### 关键实验
在Natural Questions、HotpotQA、MS-MARCO三个公开数据集上测试，对比Vanilla RAG、TrustRAG、RobustRAG基线：黑盒投毒下攻击成功率（ASR）从67%/87%/64%降至3%/14%/4%，白盒HotFlip攻击ASR从~74%降至27.8%，毒文档MRR降至0，正常查询准确率从被攻击后的13-33%恢复到58-76%；L1+L2默认配置仅增加12ms/query latency，比同类方案低36倍。

### 最值得记住的结论
检索投毒的核心脆弱点是毒文档必须同时满足召回相似度、触发-payload结构、生成误导三个约束，正交多维度校验的防御成本远低于攻击者同时满足多约束的攻击成本。

---
title: 'Query Obfuscation with Embedding-Optimized Noise (EON): A Representational
  Blindspot in Agentic Retrieval'
title_zh: 嵌入优化噪声（EON）查询混淆：Agent检索的表征盲区漏洞
authors:
- Ankit Gupta
- Christoph Adami
- Emily Dolson
affiliations:
- Michigan State University
arxiv_id: '2611.31344'
url: https://arxiv.org/abs/2611.31344
pdf_url: https://arxiv.org/pdf/2611.31344
published: '2026-11-23'
collected: '2026-11-25'
category: Agent
direction: Agent检索安全 · 对抗样本构造
tags:
- EON
- Adversarial Attack
- Dense Retrieval
- Guardrail Bypass
- Agentic Retrieval
one_liner: 提出无需访问候选库的嵌入优化噪声EON，可绕过语义护栏同时保留原查询的检索结果
practical_value: '- 安全风控侧可新增轻量无意义文本检测器（如开源gibberish detector），拦截EON类无语义查询，目前实测可将文本类Bypass-ASR降至0，防御成本低效果明确

  - 高安全级别的检索链路（如电商合规检索、Agent工具调用）可替换单向量稠密检索架构，改用ColBERTv2晚交互检索+交叉编码器重排，实测可大幅削弱EON的检索结果保留率

  - 对外暴露向量嵌入接口的业务（如电商开放检索服务）需做权限管控，避免攻击者本地基于公开嵌入模型构造EON发起护栏绕过攻击'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agent、RAG系统依赖单向量稠密检索实现工具选择、记忆召回、文档检索，流程默认查询语义与嵌入表征强绑定，未考虑攻击者可构造无意义查询匹配目标嵌入，绕过语义护栏同时触发危险检索；现有攻击方案均需访问候选库或检索反馈，对纯黑盒场景的风险研究不足。

### 方法关键点
- 构造完全语料盲的EON：仅通过无梯度贪心搜索优化无意义文本/图像的嵌入，使其与原查询嵌入余弦相似度最高，全程无需访问候选库、检索结果、护栏判定结果
- 文本EON默认使用64个无意义ASCII原子构造，禁止复用原查询有意义词汇；图像EON从空白画布逐通道调整像素
- 核心评估指标：Preservation@k（原查询top1结果在EON查询topk中的占比）、Bypass-ASR@k（EON绕过护栏且保留原查询危险检索结果的联合成功率）

### 关键实验
覆盖意图路由、工具选择、文档检索、Agent记忆召回、跨模态检索7类任务，测试BGE、Qwen3-Embedding、CLIP、DINOv3等主流嵌入模型，对比随机噪声、HotFlip梯度攻击等baseline：
1. 意图路由、工具选择场景Preservation@1最高达90.8%，恶意查询场景绕过Qwen3Guard-8B护栏的Bypass-ASR@1最高达82.2%
2. 模拟媒体Agent检索链路，加入50%良性干扰项后，EON仍能以90%概率召回NSFW类目标内容
3. 加入无意义文本检测器或改用晚交互检索+交叉重排架构，可完全消除文本类EON攻击效果

### 核心结论
语义可识别性与嵌入表征的可操作性存在天然割裂，单向量稠密检索系统不能仅用嵌入相似度作为查询安全或语义合法的判断依据

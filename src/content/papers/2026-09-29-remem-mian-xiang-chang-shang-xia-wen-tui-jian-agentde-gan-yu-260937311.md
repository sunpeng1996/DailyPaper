---
title: 'ReMem: Rethinking Perception and Memory in Long-Context Recommendation Agents'
title_zh: ReMem：面向长上下文推荐Agent的感知与记忆优化框架
authors:
- Haohao Qu
- Yongcheng Jing
- Chun Hin Chan
- Shanru Lin
- Wenqi Fan
- Dacheng Tao
affiliations:
- The Hong Kong Polytechnic University
- Nanyang Technological University
arxiv_id: '2609.37311'
url: https://arxiv.org/abs/2609.37311
pdf_url: https://arxiv.org/pdf/2609.37311
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: 长上下文推荐Agent · 感知与记忆优化
tags:
- RecAgent
- LongContext
- OCR
- DynamicMemory
- GRPO
one_liner: 融合OCR多模态感知、时序动态记忆与多记忆GRPO的推荐Agent框架，较SOTA平均提升5.16%
practical_value: '- 跨平台商品信息采集可弃用HTML解析方案，改用DeepSeek-OCR-2等成熟OCR工具解析商品页截图，可自动过滤广告、冗余脚本噪声，兼容APP/小程序/网页等异构布局，无需为每个平台单独开发爬取规则

  - 处理超长用户行为序列时，可复用分块动态记忆机制，固定记忆token长度，推理复杂度随序列长度线性增长，无需依赖长上下文大模型或外部向量数据库检索，降低推理成本的同时避免长上下文性能衰减

  - 多轮Agent任务训练可复用Multi-Mem GRPO设计，将最终任务收益反向传播到所有中间记忆更新步骤，解决多轮交互中信用分配难的问题，不需要额外引入复杂的辅助监督信号'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐Agent存在两个核心落地痛点：一是依赖HTML解析商品页，跨平台适配性差、噪声多，还丢失图片等多模态信息；二是超长用户交互历史+多轮交互Trace容易超出LLM上下文窗口，现有长上下文方案要么性能衰减快，要么依赖外部模块破坏原生生成流程，难以落地。
### 方法关键点
- 感知层：采用DeepSeek-OCR-2解析商品页截图，直接提取结构化多模态商品信息，过滤广告、冗余脚本等噪声，跨平台无需适配HTML结构
- 记忆层：采用分块时序动态记忆（TEM）机制，将用户历史按固定窗口分块逐块处理，每次更新固定长度的自然语言记忆，推理复杂度线性于历史长度，无需修改LLM架构
- 训练层：采用Multi-Mem GRPO算法，将最终推荐任务的收益反向传播到所有中间记忆更新步骤，解决多轮记忆更新的信用分配问题
### 关键结果
在基于Amazon Reviews 2023构建的Games、Books、MovieTV三个推荐Agent数据集上，对比SASRec、BERT4Rec、P5、ToolRec、iAgent、Mem0等8个SOTA基线，在搜索、排序、判定三类推荐Agent任务上平均较最强基线提升5.16%，超长上下文（>112K tokens）下性能衰减幅度仅为基线的1/3左右。
### 核心洞见
推荐Agent的设计应该贴合人类的浏览与认知逻辑，用视觉感知替代代码解析、用动态抽象记忆替代全量上下文存储，才能兼顾效果、效率与跨平台兼容性

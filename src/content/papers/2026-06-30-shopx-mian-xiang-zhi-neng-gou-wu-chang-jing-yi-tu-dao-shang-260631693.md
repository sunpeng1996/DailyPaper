---
title: 'ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Shopping'
title_zh: ShopX：面向智能购物场景意图到商品履约的基础模型
authors:
- Jiacheng Chen
- Tao Zhang
- Manxi Lin
- Dunxian Huang
- Teng Shi
- Honghao Fu
- Mengyan Li
- Xinming Zhang
- Chenchi Zhang
- Xuan Lu
affiliations:
- Alibaba Taobao & Tmall Group
arxiv_id: '2606.31693'
url: https://arxiv.org/abs/2606.31693
pdf_url: https://arxiv.org/pdf/2606.31693
published: '2026-06-30'
collected: '2026-07-01'
category: GenRec
direction: 生成式推荐 · 智能购物履约
tags:
- GenRec
- Semantic ID
- E-commerce Agent
- Foundation Model
- Intent-to-Item
one_liner: 统一意图理解、规划与Semantic ID原生商品操作的智能购物履约基础模型
practical_value: '- Semantic ID设计可复用混合全局-局部架构：全局RQ前缀保障LLM生成稳定性，局部VQ后缀保留属性语义可解释性，平衡生成友好度与语义召回精度

  - 训练流程可参考「SID对齐→领域增量预训练→履约SFT→多教师OPD+RL联合训练」范式，增量预训练阶段用2:1的领域/通用语料比例，避免通用能力灾难性遗忘

  - 智能购物Agent架构可放弃传统LLM调用搜推工具的模式，改用模型原生SID履约层，减少上下文压缩损失，多轮交互场景下意图保持度提升更明显

  - 评估层面可复用单/多轮生产日志构建Benchmark，结合LLM rubric打分覆盖履约质量、个性化、反馈适配等多维度，解决生成式推荐端到端效果评估难题'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有智能购物方案多采用LLM Agent封装传统搜推管线的架构，复杂意图需通过低带宽检索/排序接口传递，存在严重上下文损失；现有生成式推荐仅用Semantic ID生成召回候选，未覆盖完整的意图理解、规划、多轮履约全链路，无法适配Agent化购物的灵活交互需求。

### 方法关键点
- 架构上设计模型原生履约框架，由ShopX模型承担意图理解、路径规划、SID原生商品操作（检索、排序、搭售、对比）、接地响应生成、状态更新全流程，轻量化服务框架提供上下文访问、商品库grounding、状态管理支撑，减少跨模块损失
- Semantic ID采用混合全局-局部设计：全局向量经等价商品对比学习预训练，残差量化为2位前缀保障生成稳定性；4位局部向量从多模态商品表征量化得到，保留属性、视觉等细粒度语义，兼顾可操作性与可恢复性
- 训练流程分为四阶段：仅训练新增SID嵌入的对齐阶段；2:1比例混合领域/通用语料的增量预训练，保留通用LLM能力；履约任务SFT；多教师On-policy蒸馏+RL联合优化，适配多场景履约需求

### 关键结果数字
基于淘宝12亿商品快照、279个单轮、80个多轮生产日志构建Benchmark，对比LLM调用外部搜推工具的基线方案：单轮意图履约率提升18.2%，多轮反馈适配度提升22.7%，复杂模糊请求下整体履约效果提升21.5%，同时保留90%以上通用LLM的指令遵循与推理能力。

### 最值得记住的一句话
Agent化电商的核心瓶颈不是LLM的工具调用能力，而是意图到商品空间的低损失履约接口，模型原生的Semantic ID操作层是解决该问题的可行路径

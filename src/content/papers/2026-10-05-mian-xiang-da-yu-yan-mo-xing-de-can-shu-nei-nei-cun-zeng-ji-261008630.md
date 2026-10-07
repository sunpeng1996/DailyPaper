---
title: Towards In-Parameter Memory Augmentation for Large Language Models
title_zh: 面向大语言模型的参数内内存增强技术综述
authors:
- Haoyu Huang
- Zhongwei Xie
- Jiaxin Bai
- Yisen Gao
- Hong Ting Tsang
- Wuganjing Song
- Huihao Jing
- Yufei Li
- Yangqiu Song
affiliations:
- The Hong Kong University of Science and Technology
- Hong Kong Baptist University
arxiv_id: '2610.08630'
url: https://arxiv.org/abs/2610.08630
pdf_url: https://arxiv.org/pdf/2610.08630
published: '2026-10-05'
collected: '2026-10-07'
category: LLM
direction: 大语言模型 · 参数内内存增强
tags:
- In-Parameter Memory
- LLM
- Memory Augmentation
- PEFT
- RAG
one_liner: 按参数放置位置、获取时间双维度分类梳理大语言模型参数内内存增强技术的研究版图与开放方向
practical_value: '- 电商/推荐场景可复用IPM范式存储高频访问的商品属性、活动规则、用户偏好，对比传统RAG降低长上下文prefilling开销，解决多轮会话上下文超限问题

  - 静态领域知识优先选择离线训练的FFN层LoRA作为载体，相比嵌入层软提示知识写入更直接，推理读成本极低，适合大规模预加载

  - LLM Agent的会话级交互记忆可采用在线更新的注意力层KV内存对象存储，实现动态记忆快速读写，避免重复ICL的冗余计算成本

  - 采用IPM+RAG混合部署策略：高频复用知识写入IPM降低推理延迟，低频长尾/需溯源的知识走RAG召回，平衡效率与可解释性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM及基于LLM的Agent需加载预训练后新增的领域知识、用户偏好、交互经验，主流ICL/RAG方案依赖显式文本token注入上下文，计算与延迟随检索token数线性增长，易耗尽有限上下文窗口，KV cache压缩、稀疏注意力等优化仅能缓解无法根治该问题。参数内内存（IPM）将内存信息压缩为参数类对象，推理时直接注入前向传播，可避免长上下文prefilling的二次开销，复用场景下延迟显著降低，亟需系统梳理该领域的技术路径与适用边界。

### 方法关键点
- 按两个正交维度分类IPM技术：① 参数放置位置：嵌入层、注意力层、FFN层、混合（跨多模块注入）；② 参数获取时间：离线（部署前预先生成固定内存对象，推理时只读）、在线（服务运行中动态生成/更新内存对象，支持实时写入）
- 明确IPM三大核心要素：内存对象φ、独立的获取算子A（负责生成/更新φ）、增强算子C（负责将φ注入前向传播），划清与全参数SFT、原生KV cache、ICL/RAG的边界：仅同时满足参数化形式、独立获取算子、部署时动态注入三个条件的方法属于IPM范畴

### 核心结论
梳理覆盖50+主流IPM方法，总结不同路径的tradeoff：离线IPM读成本极低但更新需重训，适合静态通用知识存储；在线IPM可实时写入新信息但写入开销更高，适合会话级动态记忆。嵌入层IPM注入成本最低但对模型行为的影响间接，适合软提示类任务；注意力层IPM支持内容寻址，适合关联知识查询；FFN层IPM可直接改写模型事实关联，适合领域知识注入。

### 核心洞察
IPM与ICL/RAG不存在替代关系，高频复用知识走IPM降低推理开销，低频长尾/需溯源的知识走ICL/RAG保留可解释性，二者混合部署是落地最优解

---
title: 'DiffResearch: Accelerating Deep Research with Diffusion Language Models'
title_zh: 基于扩散语言模型的多智能体深度研究加速框架DiffResearch
authors:
- Alan-Barsag Gazzaev
- Alexey Gavrilov
- Mikhail Mozikov
- Sergey Muravyov
affiliations:
- ITMO University
- AXXX
arxiv_id: '2610.28909'
url: https://arxiv.org/abs/2610.28909
pdf_url: https://arxiv.org/pdf/2610.28909
published: '2026-10-19'
collected: '2026-10-23'
category: Agent
direction: 多智体科研Agent · 扩散LLM推理加速
tags:
- Diffusion LLM
- Multi-Agent
- Latency Optimization
- Deep Research Agent
- Decoding Acceleration
one_liner: 用扩散语言模型替代自回归基座实现深度研究Agent 6倍端到端提速且效果不下降
practical_value: '- 做Agent规划、子查询拆解等中间结构化输出时，可复用dFast思路：从扩散LLM的中间去噪状态提前提取可用结果，无需等生成完成，下游容忍措辞噪声的场景（如召回query生成、用户多意图拆解）可获得近2倍阶段提速。

  - 多Agent流水线中，自回归基座的核心瓶颈集中在规划、长文本生成阶段，替换为同参数量的扩散LLM基座可获得10倍左右的阶段提速，最终端到端6倍提速且效果无损，电商导购Agent、用户咨询分析Agent等互动式场景可优先评估替换收益。

  - 技术选型对比时，固定全链路脚手架、prompt、检索、评估逻辑仅切换基座的实验设计，可精准归因不同解码范式的收益，适合业务侧做AB测试的框架设计。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前主流深度研究Agent均采用自回归LLM作为基座，受左到右串行解码的固有约束，规划、长文本生成阶段延迟极高，成为交互式场景落地的核心瓶颈；扩散LLM的并行迭代去噪生成范式具备速度和全局一致性优势，但此前从未在多Agent流水线中开展受控对比验证其实际收益。

### 方法关键点
- 设计全链路扩散LLM原生的多Agent框架DiffResearch，包含9个功能Agent覆盖意图分类、查询改写、规划、检索、写作、判优全流程，基座支持一键切换扩散/自回归模型，其余组件完全复用以实现受控对比。
- 提出dFast模式：针对子查询拆解这类结构化中间输出，直接读取扩散模型的中间去噪状态，匹配到合法JSON格式结果即提前终止生成，无需等待完整解码。

### 关键结果
在Deep Research Bench的100个PhD级科研任务上测试，对比同参数量Gemma-4-26B自回归基线：扩散基座端到端延迟平均6倍提升（71.45s→11.89s），其中规划阶段提速10.7倍，写作阶段提速11.7倍，RACE效果指标与自回归基线持平甚至略优；dFast模式单独拆解子查询阶段中位数提速1.99倍，效果无损失；基于更强扩散模型Mercury的版本在公开leaderboard上排名超过OpenAI Deep Research等多个商用系统。

最值得记住的一句话：扩散LLM替换自回归基座是Agent场景降本提速的高性价比路径，其可读取中间去噪状态的特性还能为结构化中间步骤提供额外加速空间。

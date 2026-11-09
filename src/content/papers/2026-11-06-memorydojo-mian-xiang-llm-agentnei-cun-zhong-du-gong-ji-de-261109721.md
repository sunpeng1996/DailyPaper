---
title: 'MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory'
title_zh: MemoryDojo：面向LLM Agent内存中毒攻击的基准测试框架
authors:
- David H. Yang
- Blake Bullwinkel
- Amanda Minnich
- Mohammad Mohammadi Amiri
- Giorgio Severi
affiliations:
- Rensselaer Polytechnic Institute
- Microsoft
arxiv_id: '2611.09721'
url: https://arxiv.org/abs/2611.09721
pdf_url: https://arxiv.org/pdf/2611.09721
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: Agent 内存安全与对抗攻击评估
tags:
- LLM Agent
- Memory Poisoning
- Benchmark
- Adversarial Attack
- Prompt Injection
one_liner: 推出跨架构多会话LLM Agent内存中毒基准，量化不同内存系统的攻击脆弱性
practical_value: '- 搭建电商/广告导购Agent时，可参考论文中内存系统脆弱性排序选择组件：Mem0、Graphiti的抗中毒能力显著优于A-MEM、Memora、Letta，优先选低BR的系统降低被投毒风险

  - 可复用论文提出的内存感知payload优化方法：针对自身使用的内存架构特性迭代优化prompt，既可以提升合法偏好记忆的留存率，也可以反向检测对抗性投毒payload

  - 多会话Agent的安全检测可复用ISR、RSR、BR系列指标，全链路追踪恶意内容从插入、存储、检索到行为触发的全生命周期，及时清理内存中的恶意内容

  - 存储用户偏好、订单等敏感记忆时必须加写入前校验：论文显示单次恶意注入最长可在30+会话后持续生效，甚至跨任务域触发恶意行为，留存风险远高于单次prompt注入'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM Agent依赖内存系统解决长会话上下文限制问题，但恶意内容一旦被存入内存，会跨会话持续触发攻击，现有基准均固定内存架构，无法对比不同内存系统的抗中毒能力，也缺乏全链路的中毒效应量化方法。

### 方法关键点
- 构建155条多会话轨迹，覆盖4个应用领域，分同域、跨域、带50+会话历史前缀3种场景，最长包含60个会话，支持5种主流开源内存系统（A-MEM、Graphiti、Letta、Mem0、Memora）接入
- 设计全链路评估指标：插入成功率ISR、检索成功率RSR、行为触发达标率BR/BRT，还区分毒的留存（Persistence）和传播（Propagation）两种扩散路径
- 提出内存感知的payload优化方法，针对特定内存架构的读写、检索特性迭代优化投毒文本，最大化攻击成功率

### 关键结果
所有5种主流内存系统均无法完全免疫中毒攻击：未优化payload的BR最高达45.7%，经内存感知优化后BR提升2%~31%，其中A-MEM优化后BR达70.97%；跨域场景下最高仍有38.06%的同域BR，带历史前缀的高内存压力场景下Memora的BR仍达45.16%，单次注入最长可在30+会话后触发恶意行为。

**最值得记住的一句话**：内存架构是Agent安全评估必须考虑的核心变量，单次恶意内容注入可长期跨会话影响Agent行为，没有任何主流开源内存系统能完全免疫中毒攻击。

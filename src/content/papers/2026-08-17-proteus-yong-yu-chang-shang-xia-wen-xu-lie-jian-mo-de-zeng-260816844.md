---
title: 'Proteus: Incremental Memory Activation for Long-Context Sequence Modeling'
title_zh: 《Proteus：用于长上下文序列建模的增量内存激活机制》
authors:
- Reza Bayat
- Ali Behrouz
- Vahab Mirrokni
- Aaron Courville
affiliations:
- Mila - Quebec AI Institute
- Google
arxiv_id: '2608.16844'
url: https://arxiv.org/abs/2608.16844
pdf_url: https://arxiv.org/pdf/2608.16844
published: '2026-08-17'
collected: '2026-08-18'
category: LLM
direction: 长上下文LLM · 内存调度优化
tags:
- Long-Context
- Memory Optimization
- RNN
- Transformer
- Sequence Modeling
one_liner: 提出无额外开销的增量内存激活机制Proteus，可插入多种内存架构提升长上下文性能
practical_value: '- 可复用增量激活思路优化推荐系统的用户行为序列记忆模块：将用户历史行为序列按时间分段，逐步激活记忆块，解决早期行为占满内存、近期行为被挤压的问题，提升长周期用户兴趣建模准确率

  - 迁移块式内存门控方案优化Agent的长会话记忆：对会话记忆分块按对话轮次逐步解锁，无额外参数开销即可提升多轮对话历史的信息留存率，降低早期冗余信息的干扰

  - 可参考固定位置调度的工程实现思路：无需复杂学习，仅靠硬编码的位置阈值控制内存激活范围，工程落地成本极低，可快速在现有线性注意力、RNN类长上下文模型中集成'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于固定内存的长上下文序列模型存在两个核心缺陷：早期token无压缩压力，占用过多内存容量造成“状态污染”；后期token写入时易和已有存储产生干扰，导致长上下文下性能快速衰减，静态内存分配的模式本身是次优的。

### 方法关键点
- 提出增量内存激活范式：随上下文长度增长逐步扩大内存有效容量，早期用容量瓶颈强制压缩历史信息，后期解锁新内存块减少写入干扰
- 实现Proteus轻量机制：将内存划分为等大小块，采用固定的线性调度规则，按位置逐步激活前缀内存块，仅对激活块执行读写操作，无额外参数/计算开销
- 支持多架构适配：不仅可直接插入SWLA、Comba、Titans等线性内存RNN架构，还可通过嵌套学习视角扩展到Hope-Attention的MLP参数更新调度

### 关键结果
在760M、1.3B两种参数规模下对比多个SOTA基线：
1. 语言建模&常识推理：1.3B规模Titans+Proteus平均准确率从56.95提升到58.00，困惑度最低降至14.94
2. 16K长上下文NIAH任务：Titans+Proteus的UUID检索准确率从21.4提升到29.8，多键检索准确率从11.8提升到16.8
3. LongBench平均得分：Hope-Attention+Proteus从15.72提升到16.65，长上下文性能增益随序列长度增加而扩大

### 核心结论
静态内存分配本质是次优的，基于位置的容量调度是提升长上下文模型性能的低成本通用手段

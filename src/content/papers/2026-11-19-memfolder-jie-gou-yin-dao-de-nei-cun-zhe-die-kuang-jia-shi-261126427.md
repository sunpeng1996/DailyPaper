---
title: 'MemFolder: Structure-Guided Memory Folding for Efficient Agent Memory Management'
title_zh: MemFolder：结构引导的内存折叠框架实现高效Agent内存管理
authors:
- Xuyang Liu
- Chenwen Lu
- Junxi Wang
- Siyu Ren
- Xinying Lin
- Siteng Huang
- Hongli Sun
- Linfeng Zhang
- Honggang Chen
affiliations:
- Sichuan University
- Fudan University
- Sun Yat-sen University
- Zhejiang University
- Shanghai Jiao Tong University
arxiv_id: '2611.26427'
url: https://arxiv.org/abs/2611.26427
pdf_url: https://arxiv.org/pdf/2611.26427
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent 长时内存效率优化
tags:
- LLM Agent
- Memory Compression
- Retrieval Efficiency
- Long-term Memory
- Agent Optimization
one_liner: 通过双组件协同压缩Agent外部内存，低精度损失下同时降低检索与推理开销
practical_value: '- 电商导购Agent、用户长周期兴趣记忆系统可直接复用双组件架构：先用RecordFolder合并相关交互记录降低检索空间，50%记录压缩下仅损失1%性能，再用ContextFolder压缩单条内容降低推理token开销，可额外降低30%+的token消耗

  - 记录合并逻辑可迁移到用户行为序列压缩场景：实体归一化+渐进式锚点选择+语义/实体/时序三重特征融合的合并逻辑，比纯KMeans聚类合并的精度保留高3~4个百分点，适合长序列用户行为的轻量建模

  - ContextFolder的盲验证压缩机制可复用在prompt压缩场景：先提取高优先级事实做QA校验，再用约定符号集压缩内容，压缩率和事实保留率优于LLMLingua-2，适合多轮对话、用户画像prompt的离线批量压缩'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长周期运行的LLM Agent会持续积累大量外部内存记录，导致两大耦合效率瓶颈：记录数增长扩大检索搜索空间、提升检索时延，召回的多条记录拼接成的长上下文进一步升高prefill与解码注意力开销。现有剪枝方法易丢失关键信息，合并方法会生成更长的单条检索单元，无法同时优化两个维度的开销，压缩后的性能与效率trade-off较差。
### 方法关键点
- 双组件分层折叠架构：共享记录分组结果，先后降低记录数与单记录长度，适配现有各类Agent内存系统，无需重构底层架构
- **RecordFolder**：先做实体归一化消解指代歧义，再用密度峰值+ novelty 加权的渐进式锚点选择K个代表组，融合实体相似度、语义相似度与时序链特征合并同组记录，将N条原始记录压缩为K条检索单元
- **ContextFolder**：针对每组原始记录，先由Planner抽取分优先级的原子事实并生成校验QA，再由Compressor用约定符号集按目标压缩率生成紧凑编码，最后由Verifier做盲QA校验事实完整性，最多3轮迭代修正编码，确保关键事实不丢失
### 关键实验结果
在LoCoMo、PersonaMem、LongMemEval三个文本内存基准，M3-Bench-web、M3-Bench-robot两个多模态基准上测试，对比MemForest、LLMLingua-2、BabelTele等基线：
- 50%记录数压缩下，RecordFolder保留99.0%的原始性能，比最优基线高1.9个百分点；70%记录压缩下仍保留96.6%的性能
- 叠加ContextFolder后可再降低40.3%、37.9%、31%的单记录token数，检索速度最高提升5.34倍，精度损失低于2.7个百分点
- ContextFolder作为独立组件可对接其他记录压缩方法，压缩率与事实保留率优于LLMLingua-2、BabelTele
### 核心结论
Agent长时内存压缩不能只追求减少记录数或缩短单条长度，要同时兼顾检索空间和推理上下文两个维度的开销优化，基于事实校验的结构化压缩可最大化降低性能损失

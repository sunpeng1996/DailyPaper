---
title: 'Eviction as Estimation: A Fixed-Lag Smoothing View of Test-Time Memory, and
  When Measuring Beats Accumulating'
title_zh: 缓存驱逐新视角：测试时内存的固定滞后平滑框架及适用边界
authors:
- Maruthi Vemula
- Neeraj Praneeth Gajula
affiliations:
- University of North Carolina at Chapel Hill
- New York University
arxiv_id: '2607.24667'
url: https://arxiv.org/abs/2607.24667
pdf_url: https://arxiv.org/pdf/2607.24667
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: LLM推理优化 · KV cache 压缩
tags:
- KV cache
- inference optimization
- long-context LLM
- cache eviction
- fixed-lag smoothing
one_liner: 将KV缓存驱逐重定义为估计问题，提出训练无关RMM策略并明确其适用边界
practical_value: '- 长会话Agent记忆管理场景可复用固定滞后平滑思路：延迟H步后基于记忆的实际使用证据决定留存，而非仅靠到达时的特征预测，降低误删关键信息概率

  - KV cache优化场景下，RMM是H2O的严格泛化，可在内生复用明确的自定义场景（如多跳推理、工具调用链路）直接替换H2O获得收益

  - 长上下文生成/推荐场景可借鉴demonstrated utility的正确性加权思路，过滤模型错误预测阶段产生的无效注意力信号，提升核心信息识别精度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有KV cache驱逐策略（StreamingLLM、H2O、SnapKV等）均在token到达时立即决策，要么基于历史统计要么基于未来预测，无法利用后续实际使用的真实信号，在内生复用明确的场景（如Agent长会话、多跳推理）下决策精度受限，同时行业缺乏统一框架明确不同驱逐策略的适用边界。

### 方法关键点
- 将驱逐问题重定义为隐信号（token未来是否被复用）估计问题，提出commit lag轴统一现有策略：H=0对应在线过滤/预测类策略，H→∞对应离线最优Belady算法，中间区间为未被探索的固定滞后平滑域
- 定义无标注demonstrated utility信号：用近H步内正确预测的注意力和作为token真实价值的衡量，直接从模型推理过程中读取
- 提出训练无关策略RMM：新token先存入大小为H的临时缓存，待滞后H步后按demonstrated utility排序决定是否留存到正式KV缓存，是H2O的严格泛化，正确性权重全为1时完全退化为H2O

### 关键结果数字
- 受控内生复用场景：固定K=40缓存、轨迹长度达400时，RMM复用事实保留率接近1.0，远高于H2O的0.3以下、StreamingLLM的接近0
- 独立第三方基准：LongBench单-turn压缩任务中RMM与H2O性能持平，25%压缩率下TREC任务准确率比H2O高5%；LoCoMo多轮streaming场景下RMM F1为0.147，低于H2O的0.176、SnapKV的0.209

### 最值得记住的一句话
仅当token复用是清晰、局部、内生的场景下，基于实际使用测量的驱逐策略才会优于累积注意力类策略，自然文本下二者性能几乎一致。

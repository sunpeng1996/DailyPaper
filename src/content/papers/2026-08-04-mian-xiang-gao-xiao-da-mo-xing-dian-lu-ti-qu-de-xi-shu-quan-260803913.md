---
title: Sparse Weight Decomposition for Efficient Circuit Extraction
title_zh: 面向高效大模型电路提取的稀疏权重分解方法
authors:
- Chuanhao Yan
- Xuhan Huang
- Yawen Duan
- Zhenfei Yin
- Hang Zhao
- Bryan Dai
- Jie Fu
affiliations:
- IQuest Research
- Safe AI Forum
- University of Oxford
- Stanford University
- Tsinghua University
arxiv_id: '2608.03913'
url: https://arxiv.org/abs/2608.03913
pdf_url: https://arxiv.org/pdf/2608.03913
published: '2026-08-04'
collected: '2026-08-05'
category: LLM
direction: 大语言模型可解释性 · 电路提取
tags:
- Sparse Weight Decomposition
- Mechanistic Interpretability
- Circuit Extraction
- Model Reparameterization
- LLM
one_liner: 将预训练稠密线性层重参数化为两个稀疏因子，无需训练辅助网络即可高效提取可解释模型电路
practical_value: '- 电商/推荐场景部署LLM（如文案生成、Query理解大模型）时，可采用SWD对推理瓶颈线性层做稀疏分解，零数据版本无需额外校准数据，能在保真度损失可接受的前提下降低推理延迟、节省显存占用

  - 排查推荐Agent、个性化生成服务的决策错误时，可用SWD提取对应任务的核心电路，相比传统SAE、Transcoder等方法数据需求降低99%+，大幅降低可解释性分析成本

  - 做LLM LoRA微调时可参考SWD的稀疏因子设计，将LoRA低秩矩阵替换为稀疏因子，同等参数量下可提升微调效果，或同等效果下减少参数量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有大模型电路提取方法存在两大痛点：一是需训练额外稀疏表示/稀疏模型，计算开销极高，部分稀疏预训练方案需要100-1000倍于稠密模型的计算量；二是基于SVD的无训练方案提取的单元是稠密连接的，无法得到紧凑的电路结构，难以规模化落地到大尺寸LLM上。
### 方法关键点
- 提出Sparse Weight Decomposition（SWD），将预训练稠密线性权重矩阵W重参数化为两个稀疏矩阵A、B的乘积，中间共享维度作为可独立寻址的瓶颈单元，每个单元对应一条稀疏读写路径，可直接做归因、选择、消融操作
- 支持两种优化目标：带校准数据版本最小化激活重构误差，把拟合能力优先分配给模型实际遇到的输入方向；零数据版本直接最小化权重Frobenius重构误差，无需任何业务数据即可执行
- 全模型替换时仅微调稀疏因子的非零值，固定稀疏结构不改变，避免误差累积同时保留稀疏连接特性
### 关键结果
- 对比Transcoder、VPD等基线，在GPT-2、Qwen2.5、Qwen3.5-27B上测试，达到相同模型保真度时，SWD仅需基线不到1%的训练/校准数据
- 相同电路充足性、必要性指标下，SWD所需的活跃读写边数远低于所有基线
- 全量替换GPT-2所有注意力、MLP线性层后，仅需20.6M tokens微调，即可达到需2.884B tokens训练的稀疏预训练模型同等的CE损失
### 核心结论
稀疏的读写连接结构而非矩阵分解本身，是SWD能够提取更紧凑可解释电路的核心原因

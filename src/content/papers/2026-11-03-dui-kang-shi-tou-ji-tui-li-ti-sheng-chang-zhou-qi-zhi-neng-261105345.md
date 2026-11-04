---
title: Adversarial Speculative Reasoning Improves Long Horizon Agents
title_zh: 对抗式投机推理提升长周期智能体推理性能
authors:
- Hongyin Luo
- Wei Fang
- Lijie Yang
- Owen Stepan
- Daniel Suit
- Jeff Krapf
- Dana Wensberg
- Jack O'Brien
affiliations:
- Subconscious Systems Technologies, Inc.
- Massachusetts Institute of Technology
- Princeton University
- Northeastern University
arxiv_id: '2611.05345'
url: https://arxiv.org/abs/2611.05345
pdf_url: https://arxiv.org/pdf/2611.05345
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: 长周期Agent · 投机解码精度优化
tags:
- Speculative Decoding
- Long-Horizon Agent
- DPO
- KV Cache
- LLM Inference
one_liner: 反向训练投机解码Draft模型，无需改动目标LLM即可提升长周期Agent推理准确率
practical_value: '- 低本优化长链路Agent：投机解码的Draft模型可作为精度分配工具，仅训练0.06%~0.28%的总参数，无需改动大模型权重即可优化电商导购、复杂客服等长周期Agent效果，性价比极高

  - 关键节点精度分配：可复用「识别业务关键决策点+反向DPO训练」思路，将推荐/搜索长会话、多轮Agent的关键决策节点（如加购决策、query改写分叉点）引导到KV
  cache最低噪声slot生成，减少长链路误差累积

  - 工程噪声量化：可复用该研究的slot噪声测量方法，验证线上LLM服务在低精度推理、量化KV cache下的噪声增长规律，针对性优化长任务推理稳定性

  - 速度影响可忽略：该方案最多带来2%的解码速度下降，几乎不影响线上响应延迟，可快速落地验证'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
此前投机解码仅被视为纯系统优化手段，目标是最大化Draft模型接受率以提升解码速度。但实际生产部署中，LLM普遍使用低精度权重、量化KV cache、稀疏Attention，验证块内数值噪声随slot位置后移逐增约4%/slot，长周期Agent（数百轮交互、数十万token）的关键决策如果落在高噪声slot，误差会持续累积，30轮后输出分布就会出现显著偏移，大幅降低推理准确率。

### 方法关键点
- 核心思路：利用Draft模型的拒识机制，将关键决策点的token引导到验证块slot 0（噪声最低，与单token解码精度一致）生成，非关键token正常走投机解码提速
- 决策点处理：从Agent轨迹中识别关键决策节点（如决策框架选择、是否执行验证的分叉点），生成fork对：同前缀下采样得到的优选决策序列与劣选决策序列
- 反向DPO训练：让Draft模型在决策点优先生成劣选序列，触发目标大模型拒识，重新采样的关键token会写入新验证块的slot 0，以最高精度存入KV cache
- 训练成本极低：仅训练Draft模型的小部分参数，占总部署参数量的0.06%~0.28%，完全不改动目标大模型权重与验证规则，输出分布与原大模型完全一致

### 关键实验
- 数据集：长周期编码Agent基准DeepSWE（113个复杂软件工程任务）、NL2Repo-Bench（104个从零构建仓库任务）
- 基线：使用原生无偏Draft的标准投机解码方案
- 核心结果：GLM-5.3-NVFP4在DeepSWE上通过率从60.6%提升至67.6%（+7.0pct）；DeepSeek-V4.1-Flash在DeepSWE上通过率从67.8%提升至71.8%（+4.0pct），在NL2Repo-Bench上从65.0%提升至66.4%（+1.4pct），解码速度仅下降最多2%

### 核心结论
投机解码不仅是推理加速工具，还可作为上下文精度的动态分配器，用极小的训练成本就能显著提升长周期Agent的推理性能。

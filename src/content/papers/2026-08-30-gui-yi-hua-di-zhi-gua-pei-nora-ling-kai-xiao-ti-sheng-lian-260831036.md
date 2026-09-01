---
title: Normalized Low-Rank Adaptation
title_zh: 归一化低秩适配（NoRA）：零开销提升LoRA训练性能的通用方案
authors:
- Jiale Kang
- Ziyin Yue
- Zheng Zhan
- Yangyi Huang
- Weiyang Liu
affiliations:
- Yuanshi Intelligence
- Microsoft Research
- The Chinese University of Hong Kong
- Shenzhen Loop Area Institute
- SphereLab
arxiv_id: '2608.31036'
url: https://arxiv.org/abs/2608.31036
pdf_url: https://arxiv.org/pdf/2608.31036
published: '2026-08-30'
collected: '2026-09-01'
category: Training
direction: 参数高效微调 · LoRA训练优化
tags:
- LoRA
- PEFT
- Training Optimization
- Parameter Efficient Fine-tuning
- NoRA
one_liner: 对LoRA下投影矩阵做秩维度归一化，无额外开销下全面提升LoRA训练效果与稳定性
practical_value: '- 现有业务所有LoRA微调场景（如推荐prompt生成、用户意图理解、Agent工具调用微调）可直接替换为NoRA/NoRA-init，无需修改推理逻辑，零额外成本提升微调效果与收敛速度

  - 对RL微调场景（如电商个性化文案生成的奖励优化、推荐Agent交互策略调优），NoRA比PiSSA等依赖SVD的初始化方法更稳定，避免RL训练崩溃

  - 资源有限场景优先用NoRA-init：仅对LoRA的A矩阵做初始化归一化/BIMI结构化初始化，无需训练中持续归一化即可拿到80%以上收益，实现成本极低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LoRA是当前应用最广的PEFT方案，但现有研究对其优化动力学探索不足：标准LoRA下投影矩阵A的随机初始化会导致早期梯度极不均衡、收敛慢、训练不稳定；而依赖SVD的改进方案（如PiSSA）需要额外计算、在RL场景下容易失效，亟需无额外开销的通用优化方案。

### 方法关键点
- 核心思路是对LoRA的下投影矩阵A沿秩维度做列归一化，保证每个投影向量的L2范数为1，修正LoRA隐含输入侧预条件器的尺度失衡问题，同时保持线性结构，训练后可完全合并、无推理开销
- 提供两种落地方案：① 训练过程中持续对A做归一化的完整版NoRA；② 仅初始化时对A做一次归一化的NoRA-init，后者训练逻辑和标准LoRA完全一致，几乎无额外实现成本
- 额外提供结构化初始化方案BIMI：用块单位矩阵初始化A，天然满足归一化要求，进一步提升稳定性

### 关键结果
覆盖预训练、SFT、RLVR三类场景，对比LoRA、PiSSA、DoRA、MiSS等主流PEFT方案：
- SFT场景下，NoRA相对标准LoRA在Llama-3.2-3B的GSM8K、HumanEval等任务平均得分从37.93提升到43.37，涨点5.44，灾难性遗忘率从-0.56降到+0.02，和全量微调持平
- RLVR场景下，NoRA相对标准LoRA平均得分提升1.6，而PiSSA、MiLoRA等SVD依赖方案出现严重性能崩溃
- NoRA-init就能拿到大部分收益，SFT平均得分42.38，仅比完整版NoRA低1个点

最值得记住的结论：LoRA的优化效果核心由下投影矩阵A的初始尺度决定，仅通过归一化A的列范数就能零成本大幅提升LoRA的全场景表现

---
title: Non-Commutative State Tracking with Input-Dependent Low-Rank Updates in Mamba-3
title_zh: Mamba-3 输入依赖低秩更新实现非交换状态跟踪
authors:
- Hiroki Fujii
- Masaki Yamakita
affiliations:
- Institute of Science Tokyo
arxiv_id: '2609.28273'
url: https://arxiv.org/abs/2609.28273
pdf_url: https://arxiv.org/pdf/2609.28273
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: SSM 序列模型 · 非交换状态跟踪优化
tags:
- Mamba
- State-Space Model
- Non-Commutative Tracking
- Low-Rank Update
- Sequence Modeling
one_liner: 为Mamba-3添加输入依赖低秩反射项，单块即可实现高性能非交换状态跟踪
practical_value: '- 电商用户行为序列建模场景中，针对顺序敏感的非交换任务（如多步操作后的意图推断、售后状态跟踪），可参考本文的秩1反射项改造方案，无需叠加多层Mamba即可提升状态跟踪精度，参数增量极小

  - 大促、直播等时序间隔不规则的行为分析场景，可复用本文的chunkwise并行训练方案，既保留RNN的时序感知能力，又能支持批量训练不损失效率

  - 现有Mamba序列编码业务做ablation时，可尝试关闭RoPE：在纯依赖操作顺序而非绝对时间的任务（如加购-领券-下单路径跟踪）上，无RoPE版本的长序列泛化能力更强，可避免不必要的相位干扰'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
原版Mamba-3的对角转移矩阵天生具备交换性，对顺序敏感的非交换状态跟踪任务（如置换组合、多步状态变更跟踪）效果极差，必须叠加多层才能勉强提升精度，参数效率极低；现有非交换序列模型要么长序列泛化性差，要么抗时序抖动能力弱，无法适配动态环境的状态跟踪需求。

### 方法关键点
- 仅在原版Mamba-3的状态更新公式中新增输入依赖的秩1反射项，保留RoPE、指数梯形离散化、门控等所有原生机制，改造代价极低
- 反射项采用广义Householder更新结构，仅新增少量投影参数，单块即可实现非对角状态转移，满足非交换状态跟踪的数学要求
- 适配chunkwise并行训练方案，将反射项的递归计算拆分为分块下三角线性系统求解，训练复杂度仍随序列长度线性增长，无额外性能瓶颈

### 关键结果
- S5非交换群词任务：单块Mamba-3+NPLR在长度64训练集准确率100%，长度128测试集准确率99.61%，远超原版4块Mamba-3的2.28%准确率
- 固定时序贝壳游戏：单块模型在训练交换次数≤16、测试≤32的条件下成功率100%，优于原版4块Mamba-3的49.31%成功率
- 时序抖动贝壳游戏：模型在96次交换下仍保持95%+成功率，128次交换下成功率87.83%，远超DeltaProduct的21.81%和GDN的23.70%

### 核心结论
仅给Mamba-3加一个输入依赖的秩1反射项，就能用单块、更少参数实现远超原版多层Mamba的非交换状态跟踪能力，还能天然抗时序抖动

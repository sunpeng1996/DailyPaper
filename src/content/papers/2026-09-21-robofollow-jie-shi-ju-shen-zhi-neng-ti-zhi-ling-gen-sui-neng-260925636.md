---
title: 'RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents'
title_zh: RoboFollow：揭示具身智能体指令跟随能力的虚假繁荣
authors:
- Chang Guo
- Yukun Xie
- Bohan Tan
- Zheng Chang
- Zhaokai Yin
- Qianli Ma
- Yingqiao Wang
- Chao Liang
- Zhipeng Zhang
affiliations:
- Shanghai Jiao Tong University
- Anyverse Dynamics
arxiv_id: '2609.25636'
url: https://arxiv.org/abs/2609.25636
pdf_url: https://arxiv.org/pdf/2609.25636
published: '2026-09-21'
collected: '2026-09-23'
category: Agent
direction: 具身Agent · 指令跟随能力诊断
tags:
- Embodied Agent
- Vision-Language-Action
- Instruction Following
- Benchmark
- World Action Model
one_liner: 提出高场景熵诊断基准RoboFollow，揭露现有具身Agent指令跟随能力的虚假性
practical_value: '- 做Agent能力评估时可复用「高熵场景+分层扰动+意图/执行解耦打分」框架，避免模型靠视觉捷径刷分，例如电商导购Agent、仓储拣货Agent的指令理解评估可构造同一场景多任务的高熵测试case，分层验证泛化性。

  - 语言驱动的交互Agent训练可参考结论：增加指令 paraphrase 变体、提升样本多样性可小幅提升泛化性，但单纯更换更强VLM、加QA co-training、CFG等常用优化手段无法从根本解决语义对齐问题，无需做无效尝试。

  - 业务落地LLM驱动的执行类Agent时，不能仅看分布内测试准确率，必须补充布局变化、语义组合变化等分布外扰动测试，否则上线后泛化性会严重不足。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有具身Agent在标准测试集上的高成功率存在假象：多数测试场景仅有一种可行任务，模型靠视觉捷径就能完成，根本未真正理解指令，现有评估既无法区分能力来源是视觉记忆还是语义理解，也无法分离语义理解错误和运动执行错误，无法反映真实指令跟随能力。

### 方法关键点
- 构造高场景熵基准RoboFollow：每个训练场景支持多个语义有效、运动可行的任务分支，视觉信息不足以确定任务，必须依赖指令消歧，场景熵达3.782bit，是现有LIBERO基准的4倍以上。
- 设计L0-L3四层分层诊断协议：L0测分布内性能，L1测布局变化下的视觉grounding，L2测固定布局下的语义组合泛化，L3测视觉+语义联合扰动下的泛化。
- 提出多阶段意图-执行拆分打分：Intent Score测量是否选对语义目标（对象、关系、逻辑分支等），Execution Score测量选对目标后是否成功执行，分离语义理解错误和运动执行错误。

### 关键实验结果
测试9个主流VLA（π0/π0.5、GR00T、OpenVLA等）和WAM（Motus、FASTWAM）模型：所有模型L0下Intent Score可达90%~100%，但L1~L3下Intent Score平均暴跌至30%~55%，π0在空间关系场景L1下Intent Score直接降至0%；测试更强VLM、QA co-training、LangForce、CFG等常用优化手段，均无法缩小泛化差距；增加指令变体从1个到5个，可将L3 Intent Score从41.5%提升到53%，但仍存在较大差距。

### 核心结论
现有具身Agent的指令跟随能力大多是视觉捷径驱动的伪能力，分布内高准确率不代表真的理解了指令，必须在高熵扰动场景下验证才能得到真实能力。

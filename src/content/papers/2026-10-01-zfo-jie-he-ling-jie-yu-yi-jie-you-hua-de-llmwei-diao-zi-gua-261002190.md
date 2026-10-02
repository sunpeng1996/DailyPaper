---
title: 'Trust the Direction, Search the Step: Zero-and-First-Order Methods for LLM
  Fine-Tuning'
title_zh: ZFO：结合零阶与一阶优化的LLM微调自适应步长选择框架
authors:
- Cristian McGee
- El Houcine Bergou
- Aritra Dutta
affiliations:
- University of Central Florida
- Mohammed VI Polytechnic University
arxiv_id: '2610.02190'
url: https://arxiv.org/abs/2610.02190
pdf_url: https://arxiv.org/pdf/2610.02190
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: LLM训练 · 自适应步长优化
tags:
- LLM Fine-Tuning
- Zeroth-Order Optimization
- First-Order Optimization
- Adaptive Step Size
- Training Stability
one_liner: 解耦一阶优化方向与零阶步长选择，仅增2次前向传播提升LLM微调性能与稳定性
practical_value: '- 业务侧做电商文案生成/大模型推荐排序/Agent工具调用微调时，可直接将ZFO作为AdamW等一阶优化器的轻量Wrapper，仅新增2次前向传播开销，就能大幅降低学习率调参成本，同时提升训练稳定性，尤其适配RLHF/GRPO等易不稳定的微调范式

  - 优先选用Padé3作为ZFO的局部模型，论文验证其在14/16的LLM微调场景下优于固定步长AdamW，无需额外验证即可直接复用该配置

  - ZFO的额外开销极低：时间仅增5.2%、GPU内存仅增11%~19%，无需修改现有训练管线即可快速落地，适合资源紧张的LoRA微调场景

  - 对于对模型效果稳定性要求高的上线场景，ZFO可有效降低不同随机种子的效果方差，减少上线前的重复实验成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM微调的步长选择是长期核心痛点：固定学习率或人工调度的步长要么收敛速度慢，要么容易导致训练崩塌；全量线搜索成本过高无法适配大模型场景。现有一阶优化器输出的更新方向准确性高，但步长的最优取值难以预先确定；纯零阶优化方法在高维参数空间噪声大，效果远不如一阶方法。
### 方法关键点
- 方向与步长解耦：由一阶优化器（AdamW/Muon）输出可信的更新方向，仅沿该方向做2次对称的零阶前向探针，无需额外反向传播
- 利用共享batch样本做中心差分，估计二阶、三阶方向导数，支持二阶/三阶Taylor、二阶/三阶Padé共4种局部模型拟合单维度目标函数，在预设的bounded区间内选择最优步长，Padé模型增加极点检测，异常时fallback到二阶Taylor模型保证稳定性
- 整个框架可作为任意一阶优化器的插件使用，不改变原有训练逻辑
### 关键结果
对比固定步长AdamW、MeZO零阶微调baseline，覆盖Qwen-2.5-Math、Phi-2、Gemma-2、Llama-3.2等1-2B级模型，16个推理数据集：
- Padé3实例在14/16的场景下超过AdamW baseline，Qwen-2.5-Math-1.5B在MATH数据集准确率从31.77%提升至39.58%，OpenBookQA从26.07%提升至64.07%，最大提升38个百分点
- 额外开销极低：单迭代时间仅增5.2%，GPU内存仅增11%~19%，远低于全量线搜索成本
### 核心结论
一阶优化输出的方向已足够可靠，仅用极低的零阶探针成本沿该方向自适应选步长，就能以极小开销大幅提升LLM微调的性能与稳定性

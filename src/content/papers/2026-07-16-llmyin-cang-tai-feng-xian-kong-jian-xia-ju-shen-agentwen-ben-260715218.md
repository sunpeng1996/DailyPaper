---
title: 'When Words Are Safe But Actions Kill: Probing Physical Danger Beyond Text
  Safety in Hidden-State Risk Space'
title_zh: LLM隐藏态风险空间下具身Agent文本外物理危险探测
authors:
- Weimeng Wang
- Ziqiang Wang
- Zihang Zhan
- Chuanpu Fu
- Qi Li
- Ke Xu
affiliations:
- Tsinghua University
- Nanyang Technological University
arxiv_id: '2607.15218'
url: https://arxiv.org/abs/2607.15218
pdf_url: https://arxiv.org/pdf/2607.15218
published: '2026-07-16'
collected: '2026-07-17'
category: Agent
direction: 具身Agent安全 · LLM隐藏态探针
tags:
- Embodied Agent
- Hidden State Probing
- LLM Safety
- Physical Risk Detection
- Linear Probe
one_liner: 验证LLM隐藏态内容与物理危险信号可分离，提出轻量探针PRISM实现低误判具身安全检测
practical_value: '- 做Agent安全模块时可替换LLM-as-judge方案：基于LLM中后层隐藏态训练单线性层PRISM探针，推理速度提升1.8~2.1倍，误判率降低50%以上，适配低延迟/端侧Agent场景

  - 电商/内容平台的隐性风险识别可借鉴CD/PD分离思路：针对字面无风险但实际存在操作风险的咨询/指令（如高危商品操作指导），单独训练物理风险隐藏态探针，比通用内容安全模型漏判率低近100%

  - 风险检测类数据集构建可参考PSB-1K的最小对比对设计：完全移除显性风险关键词，保证模型检测的是真实逻辑风险而非匹配关键词作弊'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM已广泛应用于具身Agent的上层任务规划，现有文本安全机制仅能识别字面带违规表述的内容危险（CD），对字面完全无害但落地到物理世界会产生风险的物理危险（PD）存在明显缺陷：通用内容安全模型完全无法识别PD，零样本LLM judge虽能做到PD高召回，但会严重过杀正常任务，FPR最高达39%，无法直接落地。

### 方法关键点
- 信号可分性验证：通过隐藏态方向分析和随机拆分空值检验，证明CD和PD在Qwen2.5、Phi-3.5、SmolLM2等主流LLM的中后层隐藏态中为独立可分离信号，两者探针权重夹角稳定在70~78°，显著高于随机拆分基线
- PRISM探针设计：仅用单L2正则化逻辑回归层，针对交叉验证选出的最优中后层最后token隐藏态做二分类，同时覆盖CD和PD两类风险，无需额外微调LLM
- PSB-1K数据集：构造1000组最小对比家庭场景物理风险对，完全移除“危险”“伤害”等显性风险关键词，避免模型靠关键词匹配作弊

### 关键结果
在SafeAgentBench基准上，PRISM在Qwen2.5 3B/7B/14B/32B全系列上准确率达86.2~87.7%，FPR仅11.7~13.7%，比同规模LLM judge的FPR低50%以上，推理速度提升1.86~2.12倍；在无显性风险关键词的PSB-1K上，PRISM准确率达99.6%，FPR仅0.7%，而同规模LLM judge FPR高达67.8%，Llama Guard 3完全无法识别PD风险。

### 核心结论
具身Agent的物理安全并非文本安全的子任务，而是独立存在于LLM隐藏态的可探测信号，轻量线性探针即可实现比大模型judge更优的精度-效率trade-off

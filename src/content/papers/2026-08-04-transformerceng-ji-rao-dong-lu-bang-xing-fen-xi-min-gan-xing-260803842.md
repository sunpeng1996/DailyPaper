---
title: 'Sensitivity, Causality, and Repair Dissociate: A Layer-Wise Analysis of Perturbation
  Robustness and Its Scaling'
title_zh: Transformer层级扰动鲁棒性分析：敏感性、因果性与修复能力分离及缩放规律
authors:
- Nathan Labiosa
- David Buff
- Ena Nayak
- Erica Donno
affiliations:
- University of Southern California
arxiv_id: '2608.03842'
url: https://arxiv.org/abs/2608.03842
pdf_url: https://arxiv.org/pdf/2608.03842
published: '2026-08-04'
collected: '2026-08-05'
category: LLM
direction: 大模型鲁棒性 · LoRA放置优化
tags:
- Robustness
- LoRA
- Transformer
- Perturbation
- Interpretability
one_liner: 揭示大模型扰动鲁棒性三层级指标分离规律，给出LoRA修复放置最优策略
practical_value: '- 做搜索Query纠错、用户咨询话术扰动修复的LoRA适配时，不要按激活patching、特征divergence等可解释性诊断结果选放置层，默认选择最深层窗口，避免级联破坏拉低干净输入的处理效果

  - 可通过训练零成本的LRD（层表征差异）预筛，提前排除早中层LoRA放置选项，节省大量训练算力

  - 评估涉及思维链的LLM应用（比如智能导购客服、Agent推理决策）时，必须匹配足够长的生成长度阈值，避免截断导致的虚假增益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
部署态大模型常因输入拼写错误、OCR噪声、谐音词等表面扰动失效，过往默认「表征偏离最大、激活patching恢复效果最好的层就是最优修复层」，但三类责任指标的对应关系从未被系统验证，直接指导LoRA等适配操作往往带来负向效果。
### 方法关键点
- 定义三个层级量化指标：敏感性（LRD，干净/扰动输入隐状态余弦差异）、因果性（单层激活patching的错误预测恢复率）、补偿能力（层窗口LoRA修复的准确率增益）
- 覆盖5个主流开源大模型，归纳出两类扰动传播模式：spike-and-suppress（早层差异大、中层被吸收）、late-accumulation（差异随层数累加、随模型规模扩大特征更显著）
- 通过层扫实验验证级联破坏机制：早层LoRA适配会破坏下游所有干净输入的正常计算
### 关键结果
- 2个达到80% identity-patch阈值的模型中，敏感性与因果性呈强负相关（ρ=-0.72~-0.88），三类指标峰值完全不重合
- LoRA放置在诊断指向的早中层时准确率最高下降7.8pp，仅最深层放置无负向损失，比全层适配的准确率损失低9~14pp
- 短生成长度预算下评估的表征稳定性损失看似有+7.3pp增益，换足够长预算后反转为-3.5pp，属于截断导致的方法学伪影
### 核心结论
大模型扰动修复时，可解释性诊断指出的「问题层」反而是最差的LoRA放置位，默认选最深层、匹配足够长的生成评估阈值才是可靠实践

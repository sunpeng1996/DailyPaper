---
title: Recursive Harness Self-Improvement for Frontier Reasoning Data Synthesis
title_zh: 用于前沿推理数据合成的递归工具链自优化框架
authors:
- Wenlong Zhang
- Zhengbo Jiao
- Chenxu Zhang
- Lekang Jiang
- SiYuan Ma
- Qituan Zhang
- Guo Chen
- Linfeng Zhang
affiliations:
- Shanghai Jiao Tong University
- University of Science and Technology of China
- Imperial College London
- University of Cambridge
- Nanyang Technological University
arxiv_id: '2610.03548'
url: https://arxiv.org/abs/2610.03548
pdf_url: https://arxiv.org/pdf/2610.03548
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 推理数据合成 · 递归自优化
tags:
- Synthetic Data
- Recursive Self-Improvement
- Reasoning LLM
- Harness Evolution
- Data Generation
one_liner: 提出任务-生成工具链协同进化框架，无需调整模型权重即可生成难度递增的高价值推理训练数据
practical_value: '- 做生成式推荐/Agent的训练数据合成时，可复用任务-工具链协同进化思路，无需调整大模型权重，仅迭代prompt、技能库、生成流程，即可逐步生成更贴合长尾需求的样本，降低数据合成成本

  - 可直接复用在线+离线双阶段更新策略：生成过程中将推理失败case转化为可复用构造技能实时生效，每批生成后整体迭代流程，经验证达标才上线，兼顾迭代效率与生成质量

  - 可参考候选验收的成本约束规则：允许成本随难度增益线性提升，最高不超过基线的1.5倍，平衡生成样本质量与算力成本，适配业务侧合成数据生产的ROI要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有推理数据合成方法大多仅递归复用生成任务作为种子，生成工具链全程固定，无法随任务分布变化持续提升样本难度，单纯扩大数据集规模也无法满足前沿推理模型对高挑战性样本的训练需求。
### 方法关键点
- 提出任务-工具链协同进化框架，工具链包含可复用构造技能、角色prompt、生成流程，全程固定模型权重与验证逻辑，仅迭代工具链组件
- 双阶段自更新：在线更新将生成过程中求解器失败的推理轨迹转化为可复用构造技能，实时生效；批量生成后离线更新优化技能、prompt、流程，候选工具链需满足生成任务难度更高、有效性不下降、成本涨幅不超过1.5倍且匹配难度增益才会被采纳
- 内置回滚机制，工具链迭代失败时自动回滚到上一有效版本，保证生成稳定性
### 关键实验结果
跨数学、代码、科学3个领域共150条种子链迭代14轮，固定求解器DeepSeek-V4-Pro的准确率从100%降至54.8%；对比固定工具链递归的73.5%、仅在线更新的67%、仅离线更新的59%，难度提升幅度显著。下游训练中，10K合成数学样本微调27B模型后APEX基准mean-16准确率达62.5%，超过DeepSeek-v4-pro、Gemini 3.1 Pro等前沿模型；合成数据用于SFT/GRPO训练，多个基准精度普遍提升4pp以上。
### 核心结论
生成数据的难度天花板往往由生成工具链的能力决定，而非底层模型的能力上限，迭代生成工具链相比调整模型权重成本更低、收益更可控

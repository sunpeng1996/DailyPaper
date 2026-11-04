---
title: 'ReSI-Math: Exploring Recoverable Capability Frontiers for Efficient Reasoning
  Improvement'
title_zh: ReSI-Math：探索可恢复能力边界实现高效推理提升
authors:
- Yao Cui
- Zhen Yang
- Yuandong Wang
- Yangfu Zhu
- Tianyu Wo
- Zhenzhou Shao
affiliations:
- Capital Normal University
- Tsinghua University
- Beihang University
arxiv_id: '2611.04787'
url: https://arxiv.org/abs/2611.04787
pdf_url: https://arxiv.org/pdf/2611.04787
published: '2026-11-03'
collected: '2026-11-04'
category: Reasoning
direction: 推理优化 · 可恢复能力边界
tags:
- RLVR
- Evolutionary Search
- Mathematical Reasoning
- GRPO
- LoRA
one_liner: 通过自评判引导的进化搜索挖掘可恢复能力边界，以极低数据成本提升LLM数学推理性能
practical_value: '- 做低数据RL微调（比如电商导购Agent垂域适配）时，可复用frontier-guided样本选择策略：优先选当前模型成功率中等、输出分歧大的样本训练，比随机选择提升效率高30%+，大幅节省标注成本

  - 做Agent推理自修复模块时，可借鉴Self-Judge引导的轨迹交叉方案：不用微调参数，仅通过重组多轮推理轨迹就能恢复40%左右的错误推理结果，适合实时推理场景的错误兜底

  - 构建多角色LLM系统（如电商智能客服的求解器+质检评判器）时，可复用双RLVR训练范式：用推理过程中评判器和实际结果的误差同步优化评判模块，无需额外标注数据即可提升评判准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前基于RLVR的LLM推理提升方案普遍存在训练数据利用率低的问题，且默认模型答错就是能力不足，但大量实践表明，很多推理错误是解码随机因素导致的，固定参数下通过轨迹搜索即可恢复，此前没有成熟框架将这种可恢复能力转化为高效训练信号。
### 方法关键点
- 定义**可恢复能力边界**：固定模型参数时，直接解码正确率低，但通过有限轨迹重组即可得到验证正确解的问题集合，是模型最易通过少量训练掌握的目标区间
- 四步迭代流程：①Elicit：对候选问题采样16轮推理轨迹，划分正确/错误集；②Repair：用Self-Judge引导进化交叉重组轨迹，挖掘可恢复的失败案例；③Consolidate：选边界问题做单样本GRPO微调求解器，同时用自评判和验证器的不一致信号微调评判器；④Reprofile：每次模型更新后重新评估候选池，动态选下一个边界样本迭代
### 关键结果
基于Qwen3-VL系列基座测试：①正确-错误轨迹交叉的后代正确率达43.8%；②3轮单样本RLVR后，8B模型在MATH500、WE-MATH平均得分从78.71提升至80.16；③单样本训练场景下，边界引导选样比随机选平均得分高0.85个点，远优于固定顺序训练、全量批量训练方案。
### 核心结论
模型的推理错误不全是能力缺失，挖掘处于可恢复边界的样本，能以极低数据成本实现推理能力的稳定提升

---
title: 'DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents'
title_zh: DeLoop：基于重复动作自监督的长序列Agent循环优化
authors:
- Tianle Chen
- Pushkar Singh
- Ketan Todi
- Biswajit Paria
- Qijia He
- Wenqi Wang
- Yuwen Tan
- Jike Zhong
- Sugato Basu
- Deepti Ghadiyaram
affiliations:
- Google
- Boston University
- University of Washington
- University of Southern California
- Google DeepMind
arxiv_id: '2610.19376'
url: https://arxiv.org/abs/2610.19376
pdf_url: https://arxiv.org/pdf/2610.19376
published: '2026-10-13'
collected: '2026-10-22'
category: Agent
direction: 长序列Agent · 自监督去循环优化
tags:
- LLM Agent
- Long-Horizon
- DPO
- Self-Supervised
- Loop Reduction
one_liner: 自挖掘Agent轨迹中循环/破循环动作对做DPO训练，无额外标注下大幅降低长序列Agent循环率
practical_value: '- 电商导购/搜索Agent场景可复用循环判定规则：归一化工具调用后与历史<调用参数，返回结果>做匹配，完全一致即判定为无效循环，无需标注即可快速拦截重复请求，降低工具调用成本

  - 长交互Agent（如多轮客服Agent、长路径搜索Agent）可从自有业务轨迹自动挖掘<循环动作，破循环动作>正负对，用LoRA+DPO做低成本微调，无需人工标注即可减少无效步骤、提升任务成功率

  - 该自监督方法无需任务奖励、黄金标注、LLM打分，可与现有上下文压缩方案（LLMLingua、摘要压缩等）直接结合，在不改动现有记忆架构的前提下降低循环率，效果优于推理侧加重复拦截器'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长序列LLM Agent在上下文压缩适配有限窗口时极易出现循环问题：重复调用相同工具得到完全一致的观测，既浪费算力、增加交互成本，还会使任务失败率平均提升26个百分点。现有解决方案要么优化上下文记忆策略治标不治本，要么依赖人工标注、LLM打分、任务奖励做训练，落地成本高。

### 方法关键点
- 循环自动判定：对每个步骤的工具调用做格式归一化，与历史步骤的<归一化调用参数，观测值>签名对比，完全一致即判定为循环动作
- 自监督正负对挖掘：从同一Agent的交互轨迹中，取循环动作作为负例，该轨迹后续第一个打破循环的非重复动作作为正例，无需任何外部标注、任务奖励或LLM judge
- 训练策略：基于DPO训练Agent偏好破循环动作，仅需LoRA微调即可，无需改动原有Agent推理框架

### 关键结果
在CodeGym基准测试对比10+基线（包括上下文压缩方案、推理侧重复拦截器、有监督SFT/DPO等）：
- Qwen3-8B压缩场景下，循环率从57.3%降至6.1%，单任务步骤数降至原1/3，任务成功率基本持平；加入跨域数据的DeLoop-Mix可进一步提升成功率5.2个百分点
- 大模型上收益更明显：Qwen3-32B循环率从38.5%降至12.9%，任务成功率从37.7%提升至44.8%
- 效果泛化到ALFWorld、AppWorld等4个Agent环境，所有场景循环率均显著下降

最值得记住的一句话：Agent自身的失败轨迹本身就是高质量自监督信号，无需额外标注即可实现性能优化。

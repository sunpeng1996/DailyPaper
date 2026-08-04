---
title: 'Hear, Invoke, and Understand: A Skill-Calling Multimodal Agent for Large Audio
  Language Models'
title_zh: 面向大音频语言模型的技能调用多模态音频Agent SpeechAgent-R
authors:
- Yuwen Wang
- Tian-Hao Zhang
- Minghao Cai
- Yilin Ren
- Ziyang Jiang
- Xin Wang
- Zhichao Wang
- Pan Zhou
- Kun Zhan
- Xinyuan Qian
affiliations:
- 北京科技大学
- 理想汽车
arxiv_id: '2608.01881'
url: https://arxiv.org/abs/2608.01881
pdf_url: https://arxiv.org/pdf/2608.01881
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 多模态音频Agent · 工具调用与技能编排
tags:
- Multimodal Agent
- Audio LLM
- Tool Calling
- SFT
- RL
- Audio Reasoning
one_liner: 基于轨迹SFT与多轮RL训练的音频Agent，可协调外部工具解决复杂声学任务，泛化性显著提升
practical_value: '- 做电商语音交互类Agent（语音导购、售后语音客服等）时，可复用「轨迹级SFT+GRPO RL」两阶段训练范式，先通过高质量交互轨迹学习结构化工具调用逻辑，再用RL优化多轮决策，效果显著优于仅监督最终回答的训练方式

  - 工具调用类Agent的奖励权重可参考论文配比：0.05（输出格式）、0.25（工具交互正确性）、0.7（最终回答质量），平衡工具调用准确率和业务目标，避免冗余调用或格式错误

  - 评估垂类Agent泛化能力时，可参考HIU-Bench的ID/OOD拆分设计，单独衡量工具选择、交互流程、回答质量三个维度，更贴近真实业务中未见过场景的表现

  - 对于复杂音频理解场景（嘈杂环境语音搜索、多说话人会话语义抽取等），可通过技能抽象+动态工具编排的方式扩展能力，无需把所有声学能力都塞进基座，降低训练和迭代成本'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有大音频语言模型（LALMs）仅依赖训练阶段获取的参数知识，无法在推理时调用外部声学工具解决混合语音分离、多说话人语义理解等需要多步操作的复杂声学任务，同时缺乏专门评估音频Agent工具调用能力与OOD泛化性的基准，限制了音频交互类产品的落地。
### 方法关键点
- 构建HIU-Corpus：包含65492条交互轨迹、507.6小时音频，覆盖24类任务、8种技能、9种工具，完整保留多步工具调用的决策链路
- 两阶段训练范式：第一阶段做轨迹级SFT，仅监督Agent生成的token，对技能选择、工具调用相关token加权提升优先级；第二阶段采用GRPO多轮RL优化，奖励函数按0.05/0.25/0.7的权重融合格式正确性、工具交互质量、回答质量三个维度
- 推出HIU-Bench评估基准：包含1395条样本、56类任务，拆分ID/OOD子集，OOD子集与训练集无工作流、工具重叠，可同时评估任务效果、交互质量、泛化能力
### 关键结果
以Qwen3-Omni-Thinking为基座，对比Kimi-Audio、Gemini 3系列等8个基线模型：ID任务得分84.17，较同基座Agent基线提升15.40点；OOD任务得分70.94，较基线提升14.23点；整体得分80.05，比仅做答案监督SFT的版本高13.48点。
### 核心结论
音频Agent的能力瓶颈主要不在工具本身的效果，而在于Agent对技能的理解、工具的动态编排与返回结果的多模态融合能力

---
title: 'Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements'
title_zh: Agentic ESOpt：仅需推理级显存的长时序LLM Agent全参数微调框架
authors:
- Zhi Zheng
- Rongsheng Chen
- Yunpeng Ba
- Zhenkun Wang
- Yee Whye Teh
- Wee Sun Lee
affiliations:
- National University of Singapore
- Southern University of Science and Technology
- University of Oxford
arxiv_id: '2608.17310'
url: https://arxiv.org/abs/2608.17310
pdf_url: https://arxiv.org/pdf/2608.17310
published: '2026-08-17'
collected: '2026-08-19'
category: Agent
direction: 长时序LLM Agent 无反向传播高效微调
tags:
- Evolution Strategy
- LLM Agent
- Long-Horizon Reasoning
- Efficient Fine-Tuning
- Memory Optimization
one_liner: 基于进化策略的长时序LLM Agent微调框架，仅需推理级显存，长horizon性能优于RL方法
practical_value: '- 长时序Agent（如电商多轮导购、多步用户需求拆解Agent）微调可优先用ES替代RL，解决RL长序列信用分配难、显存占用高的问题，消费级GPU也能实现大模型全参数微调

  - 可直接复用参数扰动σ的cosine衰减trick：训练时保留非0终值做正则，测试时终值降为0提升适配精度，平衡探索与利用

  - ES黑盒特性天然支持prompt-参数联合优化，电商Agent可同时进化任务prompt和模型参数，无需分开调优，提升端到端效果

  - ≥7B大模型做ES微调可尝试更小采样种群，论文显示越强的基座对种群大小敏感度越低，可进一步降低训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前长时序LLM Agent微调多采用PPO/GRPO等RL方法，存在两大核心瓶颈：一是反向传播需要存储激活值、优化器状态，显存占用极高，大模型全参数微调门槛极高；二是长轨迹下稀疏奖励的信用分配难度随horizon线性上升，效果衰减明显。现有ES方法多用于单轮推理场景，未挖掘其在长时序Agent场景的结构性优势。

### 方法关键点
- 基于进化策略（ES）设计无反向传播微调流程：每次对当前参数采样高斯扰动，用环境奖励加权更新参数，仅需存储扰动种子，显存占用等于推理级
- 引入扰动尺度σ的cosine衰减机制：训练时保留非0终值做平滑正则，测试时终值衰减到0减少优化偏差，平衡探索与适配
- 支持prompt-参数联合进化：黑盒奖励可同时用于参数更新和prompt优化，无需修改现有prompt搜索框架

### 关键实验
- 长时序数独任务：15轮horizon下，Qwen3.5-4B版本比最强RL GRPO基线高12.5%，显存仅8.41GB（比GRPO低85.7%）
- ReAct风格Math/DocVQA任务：比Qwen3.5-4B基线平均提升13.7%，比Agentic GRPO高8.3%
- WebArena-Lite任务：实现Qwen3.5-27B全参数微调，比No Skill基线高6.69%，结合Trace2Skill再提升2.42%
- 测试时自动启发式设计场景：28/36个设置下优于匹配基线

### 核心结论
ES不是RL的低成本替代品，而是长时序、稀疏反馈LLM Agent更匹配的优化范式

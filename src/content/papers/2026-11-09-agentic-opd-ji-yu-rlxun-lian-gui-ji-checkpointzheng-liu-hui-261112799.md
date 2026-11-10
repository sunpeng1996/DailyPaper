---
title: 'Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation
  for Agentic Tasks'
title_zh: Agentic-OPD：基于RL训练轨迹checkpoint蒸馏恢复LLM Agent遗忘能力
authors:
- Tingcheng Bian
- Kangye Gong
- Jinchang Luo
- MingQuan Cheng
- Feiran Liu
- Ni Li
- Xiaoling Xia
- Haiwei Wang
- Hui Li
affiliations:
- Baidu, Inc.
- Beijing Jiaotong University
arxiv_id: '2611.12799'
url: https://arxiv.org/abs/2611.12799
pdf_url: https://arxiv.org/pdf/2611.12799
published: '2026-11-09'
collected: '2026-11-10'
category: Agent
direction: LLM Agent · 遗忘能力恢复
tags:
- Agent
- GRPO
- On-Policy Distillation
- Capability Forgetting
- Checkpoint Reuse
one_liner: 利用RL训练轨迹历史checkpoint定向蒸馏，单模型恢复Agent遗忘能力且不增加推理成本
practical_value: '- 训练电商导购Agent、搜索query理解Agent、多轮推荐Agent时，不要只保留最优checkpoint，可留存全训练轨迹的checkpoint作为免费教师池，无需额外训练成本即可挖掘潜在能力

  - 可复用HCN+LAD蒸馏范式：HCN动态选择覆盖学生未解决问题最多的教师，LAD仅在学生失败、教师更优的局部做蒸馏，避免覆盖学生已掌握能力，适合小参数Agent模型提效

  - 电商搜索/推荐场景的RL训练（如排序策略RL、导购对话RL）后，可追加一轮Agentic-OPD训练，无需额外标注数据即可提升2-7个百分点效果，推理侧仅用单模型无额外成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent主流采用GRPO等RL范式训练，通常仅保留最优验证集checkpoint，丢弃其余训练轨迹checkpoint，导致大量互补能力被浪费。实测显示最优checkpoint的总问题覆盖度仅为全轨迹checkpoint覆盖度的57%-90%，存在大量被遗忘的能力可挖掘。
### 方法关键点
- 教师池构建：将单轮RL训练的所有历史checkpoint冻结构成零成本教师池，学生模型初始化为最优验证checkpoint
- HCN教师调度：每K步重评估学生能力，选择覆盖学生当前未解决问题最多的教师作为当期监督源，动态提升长期未解决问题的调度优先级
- LAD监督过滤：三层过滤逻辑：仅保留教师成功率高于学生的问题；仅采用学生失败的rollout做蒸馏；仅计算学生生成的思维/动作/回答token的KL散度损失，避免覆盖学生已掌握能力
### 关键结果
覆盖DeepSearch、工具调用、WebShop电商模拟、SciWorld、ALFWorld五大Agent域共24个基准，对比GRPO基线、模型合并、时序采样等方法：
- DeepSearch任务上，Qwen2.5-7B基线提效7.4个百分点，4B参数蒸馏后模型超过GPT-5.6、DeepSeek-V4.1等前沿大模型的DeepSearch效果
- 五大域全任务相对GRPO平均提效3-10个百分点，推理侧仅用单模型无额外成本
- 消融实验显示去掉HCN损失1.8个点，去掉LAD损失2.6-2.7个点，两个模块均为核心提效点

**最值得记住的结论**：整体准确率更低的历史checkpoint依然能为学生提供有价值的局部能力补充，RL训练的历史轨迹是完全免费的能力金矿

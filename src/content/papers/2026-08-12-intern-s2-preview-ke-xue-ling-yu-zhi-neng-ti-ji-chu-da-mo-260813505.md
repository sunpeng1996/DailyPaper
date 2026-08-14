---
title: 'Intern-S2-Preview: Scientific Agentic Foundation Model'
title_zh: Intern-S2-Preview：科学领域智能体基础大模型
authors:
- Lei Bai
- Jiaqi Cao
- Chiyu Chen
- Guanzhou Chen
- Kai Chen
- Guangran Cheng
- Erfei Cui
- Xuanlang Dai
- Shengyuan Ding
- Shangheng Du
affiliations:
- Shanghai AI Laboratory
arxiv_id: '2608.13505'
url: https://arxiv.org/abs/2608.13505
pdf_url: https://arxiv.org/pdf/2608.13505
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: 科学领域大模型 · 智能体训练与架构优化
tags:
- LLM
- Agent
- Multimodal
- Reinforcement Learning
- Foundation Model
- Time Series
one_liner: 推出397B参数科学智能体基座，支持多模态理解、长周期任务与模块化领域适配
practical_value: '- 复用Memory Decoder模块化适配思路：冻结通用大模型基座，外挂小参数领域记忆模块做垂直品类（如美妆/3C）适配，避免全量微调破坏通用能力，可快速落地电商垂类Agent、生成式推荐场景。

  - 复用adaptive length regularization方法：仅对模型已掌握的query的正响应做长度惩罚，不影响难样本探索，可用于生成式推荐文案、智能客服回答优化，在准确率不变的前提下缩短推理长度、提升响应速度。

  - 复用RL训练加速方案：co-located partial rollout+在线更新投机解码draft模型的组合，可将RL训练端到端提速1.7倍，大幅降低智能体对齐的训练成本。

  - 复用多模态预训练数据过滤逻辑：用visual-gain（加入视觉信息前后的PPL差值）筛选高价值图文对，过滤电商场景下的装饰性无效图片，提升多模态召回/推荐模型的训练效率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有通用LLM缺乏科学领域多模态适配与长周期工具交互能力，传统科学多模态模型仅支持静态问答，无法支撑需要长期推理、工具调用的科学发现流程；同时大模型垂直领域全量微调易破坏通用能力，长序列RL训练存在效率低、稳定性差的痛点。

### 方法关键点
- 架构：397B基座+外挂4B Memory Decoder，轻量路由动态融合双路next-token分布，无需修改基座即可新增领域能力；新增时序编码+预测分支，支持最长30万步时序理解与数值预测。
- 预训练：并行文本+视觉预训练，解析PDF布局生成图文交错序列，用visual-gain过滤高价值样本，配套亿级规模跨模态检索pipeline增强训练数据质量。
- 训练：SFT初始化后走多任务RL+黑白盒智能体RL+在线蒸馏的统一pipeline；引入暂停续跑的partial rollout+off-policy校正、自适应长度正则、在线更新投机解码draft模型、GEPO多任务优化等trick提升RL稳定性与效率。

### 关键结果
- 外挂4B生物领域Memory Decoder，Biology-Instructions平均分从56.92提升到60.32，无需修改397B基座参数。
- 时序编码器相比上一代，最大支持输入长度从24万提升到30万步，最长序列下推理提速5~6倍，显存占用降至原版本的20%。
- 在线投机解码使RL rollout提速2倍，端到端RL训练提速1.7倍；自适应长度正则在reward持平的前提下显著缩短输出长度。

最值得记住的结论：大模型垂直领域适配不需要每次全量微调，模块化外挂记忆+动态路由的方案可在保留基座通用能力的前提下低成本扩展垂直能力。

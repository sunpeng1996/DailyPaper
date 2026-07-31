---
title: 'Beyond Borrowed Histories: Person-Aligned User Simulation for Interactive
  Role-Playing Evaluation'
title_zh: 基于个人对齐用户模拟的角色扮演Agent交互式评估框架
authors:
- Yuhang Zhu
- Mingxuan Du
- Benfeng Xu
- Jie Gao
- Lingyun Yu
- Hongtao Xie
affiliations:
- University of Science and Technology of China
- MetaStone Technology, Beijing, China
arxiv_id: '2607.27816'
url: https://arxiv.org/abs/2607.27816
pdf_url: https://arxiv.org/pdf/2607.27816
published: '2026-07-29'
collected: '2026-07-31'
category: Eval
direction: Agent 交互式评估 · 个性化用户模拟
tags:
- User Simulation
- Role-Playing Agent
- Personalized Evaluation
- LoRA
- LLM Evaluation
one_liner: 提出PALATE框架，通过个性化用户模拟器与专属评分规则实现角色扮演Agent无偏交互式评估
practical_value: '- 做电商导购Agent、虚拟客服等交互式AI评估时，可复用用户模拟器训练思路：基于用户真实交互数据做LoRA微调，替代固定prompt模拟用户，解决固定历史评估的偏差问题，结果更贴合真实体验

  - 个性化评分规则构建方法可直接迁移：从用户带满意度标注的历史对话中自动抽取个人偏好维度生成专属rubric，相比通用规则和人类判断的一致性提升约11%，可用于电商推荐/客服的个性化满意度评估

  - 评估时可采用三轨打分机制：结合通用单轮质量、整会话质量、个性化体验三个维度，既能横向对比模型通用能力，又能捕捉用户偏好差异，避免单一打分的片面性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有角色扮演Agent（RPA）评估普遍采用固定对话历史+通用评分规则的模式，存在两个核心缺陷：一是RPA输出受前置历史质量影响极大，评估结果混有历史偏差，无法反映真实多轮交互能力；二是通用评分规则无法匹配不同用户的个性化偏好，和真实用户满意度相关性低，无法衡量实际使用体验。

### 方法关键点
- 提出PALATE评估框架，分为四大模块：用户行为建模、自由交互、个性化规则构建、三轨评分
- 基于每个用户的真实对话历史，用LoRA微调训练专属用户模拟器，还原用户的交互习惯、内容偏好、退出行为，模拟器生成的回复和真人的2AFC混淆率接近0.5，几乎无法区分
- 从同一用户的带满意度标注的历史对话中自动抽取个性化评分rubric，捕捉用户专属的偏好维度
- 采用三轨打分机制：个性化体验分、通用单轮质量分、整会话质量分，多维度刻画RPA能力

### 关键实验
数据集包含300个双语角色卡片、5个用户共5133轮带满意度标注的交互数据，对比16款主流LLM。核心结果：①带用户反应的个性化评分和人类判断的一致性达0.613，比通用评分规则（0.480）提升27.7%；②固定历史评估中，高质量前置历史会让RPA得分平均提升0.21/5分，低质量历史会拉低0.13/5分，验证了固定历史的偏差问题；③16款模型无全维度优胜者，不同用户偏好的最优RPA完全不同。

### 核心结论
角色扮演Agent的核心评估单元不是孤立的模型本身，而是用户-RPA交互对，脱离真实用户偏好和交互过程的单一打分无法反映实际产品体验

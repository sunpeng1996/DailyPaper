---
title: 'Building Multilingual Bridges: Data Mixing as the Pillar of Generalization
  for In-Language Reasoning'
title_zh: 多语言语言内推理优化：数据混合是跨语言泛化核心支柱
authors:
- Mehrnaz Mofakhami
- Ananya Sahu
- Alejandro R. Salamanca
- Daniel D'souza
- Alexandre Berard
- Thomas Euyang
- Marzieh Fadaee
- Julia Kreutzer
affiliations:
- Cohere Labs
- Cohere
arxiv_id: '2609.10445'
url: https://arxiv.org/abs/2609.10445
pdf_url: https://arxiv.org/pdf/2609.10445
published: '2026-09-09'
collected: '2026-09-10'
category: LLM
direction: 多语言大模型 · 语言内推理优化
tags:
- Multilingual-LLM
- In-language-Reasoning
- SFT
- Data-Mixing
- Cross-lingual-Transfer
one_liner: 通过优化SFT数据混合策略，3.35B小模型实现60种语言93%+的语言内推理率且性能损失极小
practical_value: '- 跨境电商/多语言Agent团队可复用数据混合策略：用「英文推理数据+10%左右小语种推理数据+20-30%小语种非推理指令数据」的配比做SFT，无需为每个小语种单独训练模型，避免推理时语言强制带来的准确率损失和doomlooping问题

  - 多语言LLM微调优先选择batch级联合数据混合方案，比顺序微调、模型合并的效果更稳定，小语种推荐、多语言搜索等场景的LLM适配可直接复用该训练策略

  - 低资源小语种的推理能力可通过扩大多语言训练覆盖范围泛化，无需每个语种都标注推理数据，大幅降低跨境业务的多语言模型训练数据成本'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前主流推理LLM以英语为中心，即使用户输入为其他语言，推理过程也默认用英语，既容易丢失原语言的语义、文化细节导致准确率下降，也导致非英语用户无法审核推理链路；推理时加语言强制前缀的方案又存在小语种效果差、易出现循环生成（doomlooping）、准确率损失大的问题，缺乏低成本的跨语言推理泛化方案。
### 方法关键点
- 以3.35B参数的多语言基座Tiny Aya为基础，优化SFT的数据组成与调度策略，三类数据联合训练：英文推理数据（提供推理能力骨架）、多语言推理数据（每个语种最多5K样本，监督目标语言推理行为）、多语言非推理指令数据（低成本对齐输入-输出语言映射，防止灾难性遗忘）
- 采用双模式训练范式：推理样本带显式推理轨迹，非推理样本带空推理块，单batch内同时混合三类数据训练
- 对比验证了数据混合、顺序微调、模型合并三种多语言能力注入方案的效果
### 关键结果
- 在数学、常识推理、指令遵循、开放式生成、文化推理6类基准共60种语言上，实现93%+的语言内推理率；相比同规模加语言强制前缀的Qwen3.5-4B，L2推理率高2pct，4-gram重复率降低60%以上，低资源小语种场景准确率高25%
- 除竞赛级数学任务外，任务准确率仅损失最高2-3%，远优于顺序微调、模型合并方案的表现
- 最低资源层级（Tier4）的小语种L2推理率仍保持94%以上，跨语言表现稳定性远优于同参数级其他模型
### 核心结论
推理是语言无关的行为，无需为每个语种标注推理数据，通过谨慎的数据混合即可将推理能力迁移到各类语言中，不存在多语言诅咒

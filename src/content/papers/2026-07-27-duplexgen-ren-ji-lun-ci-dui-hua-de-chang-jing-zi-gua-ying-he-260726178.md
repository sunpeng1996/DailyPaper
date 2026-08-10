---
title: 'DuplexGen: Adaptive Synthesis of Human-AI Turn-Taking Dialogues'
title_zh: DuplexGen：人机轮次对话的场景自适应合成框架
authors:
- Takyoung Kim
- Kang-wook Kim
- Sang Hoon Woo
- Julia Hirschberg
- Gunhee Kim
- Dilek Hakkani-Tür
affiliations:
- University of Illinois Urbana-Champaign
- Seoul National University
- Columbia University
- University of California, Berkeley
- Georgia Institute of Technology
arxiv_id: '2607.26178'
url: https://arxiv.org/abs/2607.26178
pdf_url: https://arxiv.org/pdf/2607.26178
published: '2026-07-27'
collected: '2026-08-10'
category: LLM
direction: LLM对话生成 · 轮次行为偏好对齐
tags:
- LLM
- Dialogue Synthesis
- Turn-Taking
- Human Preference Alignment
- Data Augmentation
one_liner: 基于少量槽位级人类偏好标注校准LLM，生成适配不同场景的人机轮次对话数据
practical_value: '- 电商智能客服、导购Agent场景可复用「少量槽位级人类偏好标注校准LLM生成」的思路，快速适配售前/售后/议价等不同场景的对话轮次规则，无需大规模标注

  - 训练对话类Agent时，可参考该框架生成场景专属的对话训练样本，解决通用人-人对话语料缺场景规范、用户偏好对齐度低的问题

  - 主动式导购推荐等多轮交互场景，可借鉴场景自适应轮次策略，优化AI打断、等待、接话的时机，降低用户反感度提升转化'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前全双工人机交互的轮次决策模型多采用统一规则，无法适配不同场景的交互习惯；根源是训练数据存在缺陷：人-人对话语料缺少角色锚定和场景专属规范，启发式/提示生成的轮次行为未对齐人类真实偏好。
### 方法关键点
提出DuplexGen框架，仅需少量槽位级人类偏好标注即可校准LLM输出，生成适配不同场景的轮次对话数据，无需依赖大规模语料或复杂prompt工程。
### 关键结果
在6个协作/竞争类任务中，DuplexGen生成的对话轮次与人类偏好匹配度显著优于无校准prompt、纯通用人-人语料训练的方案；基于其生成数据训练的全双工模型，轮次行为完全符合人类偏好，验证了人类校准的核心作用。

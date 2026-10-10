---
title: 'MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation
  with User Intent'
title_zh: MIRA：用于文本生成音乐用户意图对齐的音乐意图精炼Agent
authors:
- Zekai Liu
- Zhilin Wang
- Xuzheng He
- Yu Cheng
- Yang Yang
affiliations:
- Shandong University
- University of Science and Technology of China
- Central Conservatory of Music
- Kunlun Tech Co. Ltd.
- Shanghai Jiao Tong University
arxiv_id: '2610.10355'
url: https://arxiv.org/abs/2610.10355
pdf_url: https://arxiv.org/pdf/2610.10355
published: '2026-10-06'
collected: '2026-10-10'
category: Agent
direction: Agent 生成式内容意图对齐优化
tags:
- Intent Alignment
- Test-time Agent
- Prompt Optimization
- Tree Search
- Text-to-Music
one_liner: 提出分维度意图验证框架与测试时Agent，提升文本生成音乐的用户意图对齐效果
practical_value: '- 可复用「分维度可验证意图拆解规则」优化生成式内容（电商文案、推荐话术、广告创意）的用户意图对齐效果，避免单一全局评分的模糊性

  - 黑盒模型测试时优化思路可迁移：对不可微调的第三方大模型/生成服务，可通过「prompt迭代搜索+结果分维度验证反馈」的闭环提升输出质量，无需侵入模型内部

  - 轨迹感知树搜索的prompt优化方法可复用，在有限调用成本约束下比暴力搜索效率更高，适合对成本敏感的生成类业务场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文本生成音乐系统仅依赖全局文本-音频相关性评分，会忽略模糊prompt中的隐含意图，也无法定位乐器、结构、节奏、情绪演变等具体维度的对齐失败问题，无法满足真实场景下的复杂用户需求。

### 方法关键点
1. 将意图对齐任务重构为满足每请求的分维度可验证规则集，覆盖用户显式要求与隐含的领域意图，分维度评分让评估具备可诊断性；
2. 构建专家标注的真实场景请求基准MuRA-Bench，用于衡量意图对齐效果；
3. 提出测试时Agent MIRA：先将用户请求拆解为验证规则，再在有限预算下对黑盒生成器做轨迹感知树搜索的prompt迭代，通过「生成-验证-反馈」的闭环优化对齐效果。

### 关键结果
在开源和商业生成后端上均显著提升意图对齐度，可让开源生成器达到Suno、Mureka等头部商业系统的同等性能表现。

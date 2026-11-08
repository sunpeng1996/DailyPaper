---
title: 'DiaHeads: Jointly Generating Coordinated 3D Dialogue Heads with Non-verbal
  Cues from Dual Audio'
title_zh: DiaHeads：基于双路音频联合生成带非语言线索的协同3D对话头像
authors:
- Jiahe Wang
- Yuxin Wang
- Xin Yun
- Binyan Chen
- Tong Pan
- Zhenjie Liu
- Shangfei Wang
arxiv_id: '2611.06970'
url: https://arxiv.org/abs/2611.06970
pdf_url: https://arxiv.org/pdf/2611.06970
published: '2026-11-04'
collected: '2026-11-08'
category: Other
direction: 双音频驱动3D对话头像生成 · 交互语义建模
tags:
- 3D Generation
- Audio-driven Animation
- Non-verbal Cues
- Dyadic Interaction
- Social Modeling
one_liner: 提出双音频联合建模的3D对话头像生成框架，引入非语言语义约束提升双人互动协调性
practical_value: '- 双数字人直播/对话场景可复用双路输入联合解码思路，让双方动作互为生成条件，消除独立生成的割裂感，提升交互真实度

  - 离散语义标签与连续生成参数在隐空间通过专家乘积融合的方法，可迁移到数字人动作/表情生成任务，强化生成结果的语义匹配度

  - 流先验替换高斯先验的设计可优化带时序依赖的生成任务连贯性，适合直播、长对话类数字人动作生成场景'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音频驱动3D头像生成方案主要针对单说话人优化，双人对话场景下未对交互双方的非语言行为语义建模，生成的互动动作协调性差，无法满足虚拟直播、游戏、影视等场景的沉浸式内容需求。

### 方法关键点
1. 双路音频拼接后联合解码，让每个对话方的动作生成以另一方的输入为条件，将交互逻辑内置到生成流程中；
2. 引入注视、摇头、点头、微笑4类离散非语言交互线索，通过专家乘积后验将离散线索与连续动作参数在共享隐空间融合，用交互语义约束连续动作生成；
3. 用流先验替换标准高斯先验，让隐层动作表征具备时序依赖性，提升动作连贯性；
4. 构建带同步FLAME参数和3D注视标注的双人对话语料CANDOR-FG。

### 关键结果
单人生成保真度与现有基线持平，双人交互协调性较单说话人及双人基线实现大幅提升；消融实验验证联合生成、流先验、多线索监督是协调性提升的核心来源；用户研究显示其优势来自用户感知的交互协调性，而非单纯的动作保真度。

---
title: 'Binary Discrete Diffusion: Candidate-Set Diffusion for Logic and Planning
  Tasks'
title_zh: 二元离散扩散：面向逻辑与规划任务的候选集扩散方法
authors:
- Rodrigo Casado Noguerales
- Dimitri von Rütte
- Bernhard Schölkopf
- Thomas Hofmann
- Aran Raoufi
affiliations:
- ETH Zurich
- Max Planck Institute for Intelligent Systems
- ELLIS Institute Tübingen
arxiv_id: '2610.28543'
url: https://arxiv.org/abs/2610.28543
pdf_url: https://arxiv.org/pdf/2610.28543
published: '2026-10-20'
collected: '2026-10-22'
category: Reasoning
direction: 离散扩散 · 推理规划任务性能优化
tags:
- Discrete Diffusion
- Candidate Set
- Logic Reasoning
- Planning
- Generative Model
one_liner: 提出以候选集为中间表示的二元离散扩散，在逻辑规划难例上显著优于现有离散扩散基线
practical_value: '- 电商搜索推荐的约束生成场景（比如合规营销文案生成、满足多约束的候选召回），可借鉴候选集中间表示思路，显式编码每个位置的多候选，支持迭代修正，提升生成结果满足业务约束的概率

  - 电商导购Agent、客服Agent的规划推理任务（比如多轮用户需求满足路径规划、异常问题排查路径生成），可复用二元对称扩散的噪声核设计，支持候选的动态增删，在复杂难例上获得更高准确率

  - 生成式推荐、序列推荐场景（比如用户个性化内容流生成、多轮推荐候选序列规划），可复用置信度引导的Ψ采样策略，优先对低置信度位置和高概率候选做修正，在降低推理成本的同时提升生成质量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有masked、uniform等离散扩散的噪声过程会一步抹除token身份，中间状态无法显式表达多候选并存的部分不确定性，在逻辑、规划等强约束、需要迭代修正的任务上表现受限，且难例上性能下降明显。
### 方法关键点
- 扩散状态采用候选token的二进制membership向量表示，支持候选逐步增删，显式表达部分不确定性
- 设计两类噪声核：对称核支持候选的移除与恢复，适配需要迭代修正的任务；吸收核仅逐步添加候选，推理时做剪枝
- 仅需常规V-way输出即可计算所有反向转移率，无需枚举指数级候选集组合，单位置复杂度保持O(V)
- 配套置信度引导的Ψ采样器，自动选择需重审的位置和候选，大幅提升采样效率
### 关键实验
在三类逻辑规划任务（Sudoku-Extreme、Boxoban、图着色）上，相同架构、训练采样预算下，二元对称扩散全量测试集准确率比masked扩散高1.3~8.3个百分点，难例上领先优势达3~59个百分点（图着色难例二元对称准确率64.13%，masked仅4.85%）；在Text8、TinyStories、OpenWebText三类文本生成任务上，与现有基线性能相当。
### 核心结论
离散扩散的corruption核设计会显著改变模型学习到的迭代计算逻辑，候选集作为中间表示可大幅提升强约束推理任务的难例性能

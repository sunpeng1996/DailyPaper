---
title: 'DistMoE: Private-data Rehearsal-free Routing in Mixture-of-Experts for Distributed
  Instruction Tuning'
title_zh: DistMoE：无私有数据排练的分布式多模态MoE指令微调框架
authors:
- Mainak Singha
- Niccolò Biondi
- Elisa Ricci
- Subhankar Roy
affiliations:
- University of Trento, Italy
- Fondazione Bruno Kessler, Italy
- University of Bergamo, Italy
arxiv_id: '2608.09907'
url: https://arxiv.org/abs/2608.09907
pdf_url: https://arxiv.org/pdf/2608.09907
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: 分布式训练 · MoE 隐私保护指令微调
tags:
- MoE
- Distributed Training
- Privacy Preserving
- MLLM
- Instruction Tuning
one_liner: 提出无需跨客户端私有数据排练的MoE路由方法，实现分布式多模态指令微调
practical_value: '- 做跨部门/多场景的MoE推荐大模型时，可复用公共锚定+残差正则的思路，不需要跨场景共享敏感用户数据，就能合并各场景独立训练的专家，规避数据合规风险

  - 多模态商品理解/图文广告生成的多场景模型迭代，可采用「StageI独立训场景专家+StageII小量公共数据校准」的流程，既保证各场景效果，又降低跨场景对齐成本

  - 想做参数高效的MoE适配时，可参考DistMoE-LoRA的设计，用轻量LoRA替代全量FFN专家，微调成本和推理成本都能大幅降低，效果下降可控'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前多模态大语言模型(MLLM)的指令微调通常依赖中心化数据访问，跨私有域数据联合训练存在合规风险；传统MoE分布式训练要么需要跨域私有数据排练来训练路由，要么独立训练的专家存在表征漂移、路由分数不可比的问题，合并后效果下降明显，亟需无需跨域数据共享的分布式MoE微调方案。

### 方法关键点
- 两阶段训练：StageI每个客户端基于公共FFN初始化私有专家，仅用本地私有数据训练私有专家和双路路由（公共/私有专家），公共FFN和注意力层完全冻结
- StageII校准：冻结所有专家，新增轻量线性适配器对齐私有专家输出与公共专家输出，引入各向同性残差正则损失约束私有专家与公共专家的残差服从标准高斯分布，用本地私有+少量公共数据校准路由参数，完全不需要跨客户端数据
- 推理阶段：平均所有客户端的公共路由参数，用标准Top-K路由动态选择公共/私有专家，支持灵活增删指定场景的私有专家

### 关键实验
在5个VQA私有数据集（COCO/GQA/OCRVQA/TextVQA/Visual Genome）上做分布式训练，对比FlexOlmo、BTX、Model Soup等基线，基于Qwen-1.8B的DistMoE在GQA上准确率达55.35%，比无校准的FlexOlmo高1.09个百分点，接近需要私有数据排练的FlexOlmo-RT基线；DistMoE-LoRA仅用极少量参数，在LLaVA-Bench野生指令测试中得分73.5，比FlexOlmo-LoRA高1.5分。

### 核心结论
将私有专家的贡献建模为相对于公共锚点的残差并做分布对齐，是实现无排练MoE专家合并的核心，在隐私优先的分布式训练场景下性价比极高

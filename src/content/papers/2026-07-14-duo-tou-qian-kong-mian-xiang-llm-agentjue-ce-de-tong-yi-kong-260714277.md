---
title: 'Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making'
title_zh: 多头潜控：面向LLM Agent决策的统一控制接口
authors:
- Amirhosein Ghasemabadi
- Ruichen Chen
- Bahador Rashidi
- Di Niu
affiliations:
- University of Alberta
- Huawei Technologies Canada Co., Ltd.
arxiv_id: '2607.14277'
url: https://arxiv.org/abs/2607.14277
pdf_url: https://arxiv.org/pdf/2607.14277
published: '2026-07-14'
collected: '2026-07-27'
category: Agent
direction: LLM Agent 轻量部署控制优化
tags:
- LLM Agent
- latent control
- model routing
- tool use
- cost optimization
one_liner: 为冻结LLM/VLM添加轻量潜态控制头，无需微调骨干即可实现低成本路由与干预决策
practical_value: '- 电商导购/客服Agent场景可复用该轻量控制头方案，无需微调大模型骨干即可快速适配新开源模型，实现本地小模型+云端大模型动态路由，最高降低90%大模型调用成本

  - 推荐系统的工具调用决策（如是否调用外部知识、用户画像补全、多轮召回）可参考Resolution Head思路，从LLM生成中间隐态判断是否需要干预，成本远低于Prompt路由或SFT微调

  - 长链路Agent任务（如电商售后多轮对话、个性化导购路径规划）可复用前缀训练的Capability Head，生成指定token数后提前判断是否切大模型/调用工具，减少无效计算降低延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent的路由、工具调用等决策依赖Prompt级路由、外部编排或任务特定微调，输入侧信号粒度粗、适配成本高，模型迭代时迁移难度大；始终调用大模型/工具则会带来过高推理成本、延迟，亟需不改动模型骨干的轻量控制方案平衡性能与成本。

### 方法关键点
- 完全冻结LLM/VLM骨干，仅挂载两个轻量控制头：Capability Head读取模型最后一层隐态轨迹，预测当前模型是否能完成任务，判断是否需要路由到更强模型或外部工具；Resolution Head读取模型中间层隐态轨迹，决策是请求补充信息、调用工具、弃权还是直接回答
- 训练阶段仅优化两个控制头：用LLM judge生成的实例 adequacy 分数监督Capability Head，用WHEN2CALL数据集的干预标签监督Resolution Head，支持前缀训练实现生成过程中的早期决策
- 推理阶段通过可调阈值控制路由与干预逻辑，可灵活适配不同业务的成本-性能需求

### 关键实验
在AndroidWorld、WHEN2CALL、TriviaQA等7个跨模态、跨任务基准上测试，对比单大模型、Prompt自路由等baseline：大小模型路由场景下，AndroidWorld最高降低90.7%大模型API成本，多基准平均降本27%~53%，同时保留95%以上大模型性能；工具调用决策场景下，TriviaQA相对得分最高提升158%，漏调用工具的情况减少65.5%，WHEN2CALL上F1最高提升11.7个点。

最值得记住的结论：LLM的隐态轨迹包含比表面输出更丰富的决策信号，基于隐态的轻量控制头是快速适配新模型、平衡Agent性能与成本的高效路径。

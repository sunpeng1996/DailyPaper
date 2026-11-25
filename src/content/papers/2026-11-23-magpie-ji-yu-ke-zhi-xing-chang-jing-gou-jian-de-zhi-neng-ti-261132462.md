---
title: 'MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction'
title_zh: MAGPIE：基于可执行场景构建的智能体多参考图像生成
authors:
- Yifan Dai
- Daili Hua
- Bohan Zeng
- Yuran Wang
- Jialing Liu
- Bozhou Li
- Chengzhuo Tong
- Yang Shi
- Kai Zeng
- Liu Yang
affiliations:
- Shanghai Jiao Tong University
- Peking University
- KlingAI Research
- Renmin University of China
- HKUST
arxiv_id: '2611.32462'
url: https://arxiv.org/abs/2611.32462
pdf_url: https://arxiv.org/pdf/2611.32462
published: '2026-11-23'
collected: '2026-11-25'
category: Multimodal
direction: 多模态图像生成 · 智能体可执行规划
tags:
- Multi-reference Image Generation
- Agent
- 3D Scene Construction
- Blender
- Multimodal Generation
one_liner: 用基于Blender可执行3D场景的智能体规划提升多参考图像生成的构图准确性
practical_value: '- 电商商品海报/主图合成场景可复用该架构：用coding agent生成可执行3D场景脚本做预校验，避免生成后构图不符合要求的返工，降低AIGC商品素材生产成本

  - 参考「先规划再生成」的两阶段范式：先通过代理渲染输出明确的构图约束，再调用生成模型生成最终内容，可提升受控生成场景的成功率

  - 多主体组合生成任务可引入显式中间校验迭代环节：通过Agent自动修正中间布局，无需人工介入即可提升多参考素材融合的准确性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
多参考图像生成需保留指定主体外观并按指令布局，现有方法无显式可校验的中间构图环节，易出现主体关系、空间布局不符合指令的问题。
### 方法关键点
1. 提出MAGPIE框架，将预期构图转化为Blender可执行3D场景程序
2. 引入coding agent关联场景实例与参考素材，校验几何、渲染视图与指令的一致性，自动修正程序消除偏差
3. 以最终代理渲染图作为可视化规划，用MAGPIE-Instruct-3K数据集训练生成器，在遵循布局的同时还原参考主体外观
### 关键结果
基于FLUX backbone时，DreamOmni2数据集上整体成功率比原生提升28.21个百分点，SconeEval数据集上取得所有参评模型最高总分，同时可兼容Qwen等主流生成基座

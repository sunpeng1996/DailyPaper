---
title: 'AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents'
title_zh: AppDeltaWorld：面向移动GUI Agent的过渡感知Delta代码世界模型
authors:
- Weikai Xu
- Yunren Feng
- Haoxiang Lei
- Kun Huang
- Yuxuan Liu
- Kang Zhao
- Xiaolin Hu
- Shuo Shang
- Bo An
affiliations:
- Nanyang Technological University
- University of Electronic Science and Technology of China
- Renmin University of China Gaoling School of Artificial Intelligence
- Xiamen University
- Independent Researchers
arxiv_id: '2608.05891'
url: https://arxiv.org/abs/2608.05891
pdf_url: https://arxiv.org/pdf/2608.05891
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 移动GUI Agent 世界模型构建
tags:
- GUI-Agent
- World-Model
- RAG
- Multimodal-Rendering
- SFT-Data-Augmentation
one_liner: 提出过渡约束的分层HTML+多模态渲染GUI世界模型，生成训练数据将移动GUI Agent性能提升至SOTA
practical_value: '- 交互类Agent模拟环境搭建可参考分层HTML+过渡约束RAG架构：通过历史跳转索引限制生成的页面范围，大幅降低状态幻觉，可直接迁移到电商APP自动化操作、业务流程测试Agent的模拟环境构建

  - 多模态UI生成可复用「代码控布局文本+扩散模型填图片槽」的混合架构，平衡生成效率与视觉保真度，可迁移到商品详情页自动生成、营销页快速改版等场景

  - 世界模型在环的SFT数据增强方法可落地：用模拟环境生成的高质量闭环轨迹补充真实交互数据，大幅降低隐私敏感场景（如用户支付流程、个人中心操作）的数据采集成本

  - 测试时无真实交互的RL适配思路可复用：无需对接真实环境即可做APP专属的策略微调，适合电商多平台、多APP场景的Agent快速适配'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
移动GUI Agent可通过视觉感知和触摸操作跨APP执行通用任务，但敏感业务、隐私场景的真实交互轨迹采集成本极高；现有GUI世界模型存在生成不稳定、模态覆盖不全、动作过渡逻辑幻觉等问题，传统模拟环境扩展维护成本高昂，无法支撑大规模Agent训练需求。
## 方法关键点
- 过渡约束分层RAG架构：将HTML拆解为一级通用结构、二级动态内容，基于动作-页面跳转索引仅检索当前动作可达的一级结构作为生成参考，从根源避免不可达状态幻觉
- 混合模态渲染Pipeline：用可执行HTML保障布局、文本的精确性，对难以用代码表达的图片区域预留插槽，通过文生图模型填充对应视觉资产，兼顾生成效率与保真度
- 世界模型在环SFT数据构造：基于真实任务种子闭环生成交互轨迹，经空白页校验、动作有效性过滤后作为训练数据，还支持测试时无真实环境交互的RL策略微调
## 关键结果
- 世界模型在CMGUIBench-500上整体得分73.51，超过GPT-Image-2、Gemini-3.1-Pro-Image等基线，UI元素/布局重建指标相对纯图像基线提升27%以上
- 生成的3.3万条轨迹训练的AppDeltaAgent-8B在AndroidLens上取得SOTA，相对Qwen3-VL-8B基线，低阶指令平均任务进度提升33.4%，高阶指令提升41.8%；MobileGym成功率从10.2%升至14.1%，MobileWorld GUI-only成功率从9.4%升至14.9%
## 核心启示
带跳转约束的结构化检索+混合模态生成的世界模型，可成为真实交互环境的低成本补充，为Agent提供高质量闭环训练数据。

---
title: 'TemplateCraft: Agentic Visual Template Generation'
title_zh: TemplateCraft：智能体驱动的可复用视觉模板生成系统
authors:
- Hongjie Yu
- Zhiyuan Fan
- Yuzhe Zhang
- Jiangcun Du
- Zhicheng Gao
- Yuhong Zhang
- Xiaokai Zhan
- Zongshi Xie
affiliations:
- Peking University
- Kuaishou Technology
arxiv_id: '2609.31451'
url: https://arxiv.org/abs/2609.31451
pdf_url: https://arxiv.org/pdf/2609.31451
published: '2026-09-25'
collected: '2026-09-28'
category: MultiAgent
direction: 多智能体协作 · 视觉模板自动生成
tags:
- Multi-Agent System
- Visual Template Generation
- Generative Media
- Workflow Orchestration
- Planner-Evaluator
one_liner: 提出多Agent架构从自然语言指令自动生成可复用的图像/视频视觉模板
practical_value: '- 可复用Planner-Evaluator分阶段回滚机制到电商短视频模板、商品图特效模板的生成Agent中，无需微调模型即可通过执行反馈迭代优化生成效果，降低人工运营成本

  - 模板生成时强制绑定持久化参考资产（风格图、动效参考等）的设计，可直接复用提升不同用户输入下的输出风格一致性，适合批量生产可复用的电商营销素材模板

  - 分阶段任务记忆+跨任务长时记忆的架构，可帮助中小团队用开源小模型搭建复杂多步骤生成类Agent，拉平与闭源大模型的效果差距'
score: 9
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
短视频/内容平台的可复用视觉模板（如人像风格化、特效模板）当前依赖设计师手动制作，成本高、响应慢，现有Agent系统多针对单次内容生成，未解决可复用模板需要的输入参数化、资产固化、跨输入效果一致性等核心问题，无法直接落地到生产场景。

### 方法关键点
- 四阶段流水线：模板规划（从技能库检索对应品类模板的通用方案）→ 素材生成（生成可替换的模拟输入+绑定到模板的持久化参考资产）→ 特效工作流生成（编排AI工具调用链路）→ 协议编译（打包成客户端可执行的模板包）
- Planner-Evaluator循环：每阶段执行后由Evaluator诊断问题，指定回滚到最早需要修改的阶段，无需全链路重新生成
- 双内存设计：任务内存存储当前任务各阶段状态，长时内存存储跨任务的错误与修复经验，无需模型微调即可迭代效果

### 关键实验
在自建的TemplateBench（60个真实生产场景的模板任务，含30个图像、30个视频任务）上测试：同Qwen3-VL骨干下，比仅Planner（best-of-3）的图像/视频模板生成成功率从56.7%/30.0%提升到66.7%/50.0%，模板符合度TA分别提升27.4%/61.9%；强制生成持久化资产可让视频模板复用一致性TR提升10%+，基于开源小模型的完整系统在视频生成成功率、符合度上超过GPT-4o-only基线。

### 核心结论
多智能体的反馈回滚+记忆复用设计，可以让开源小模型在复杂多步骤生成任务上达到甚至超过闭源大模型的效果。

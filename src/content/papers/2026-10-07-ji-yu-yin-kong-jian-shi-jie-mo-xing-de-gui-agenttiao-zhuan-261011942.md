---
title: 'Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents'
title_zh: 基于隐空间世界模型的GUI Agent跳转安全验证方法
authors:
- Jiaming Zhang
- Xuan Wang
- Fuyao Zhang
- Yang Cao
- Lingjuan Lyu
- Wei Yang Bryan Lim
affiliations:
- Nanyang Technological University
- Institute of Science Tokyo
- Sony AI
arxiv_id: '2610.11942'
url: https://arxiv.org/abs/2610.11942
pdf_url: https://arxiv.org/pdf/2610.11942
published: '2026-10-07'
collected: '2026-10-22'
category: Agent
direction: GUI Agent 世界模型安全验证
tags:
- GUI Agent
- World Model
- Latent Prediction
- Safety Verification
- Self-supervised Learning
one_liner: 无解码器隐空间GUI世界模型LGWM可毫秒级识别合法界面下的恶意跳转，性能匹敌顶级闭源VLM
practical_value: '- 电商GUI Agent（自动下单、比价、客服Agent）安全校验可直接复用LGWM方案，跳过界面生成+VLM比对流程，仅通过向量相似度计算即可完成校验，latency从分钟级降至17ms，可实现全操作链路覆盖无需抽样

  - 稀疏变化场景（GUI跳转、推荐页局部刷新、广告位动态更新）建模可复用change-weighted损失函数，提升模型对动态变化区域的注意力，避免静态内容淹没有效训练信号

  - 异常检测场景可复用「残差大小判定是否异常+残差方向判定异常类型」的双读出设计，仅需少量标注训练线性头即可区分有害/无害异常，大幅降低标注成本

  - 业务评测基准构建可参考RSWT-BENCH的donor-paired构造思路，控制单变量（如相同推荐卡片不同触发场景），避免检测器靠识别样本特征作弊，保证评测严谨性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有GUI Agent安全检测仅校验当前界面，无法识别「合法界面出现在错误跳转后」的恶意攻击（如点击查看订单却弹出登录页的钓鱼场景）；现有GUI世界模型需生成文本/代码/界面后再用VLM比对，延迟高达分钟级，无法落地全量操作校验。

### 方法关键点
- LGWM为无解码器结构的隐空间GUI世界模型，直接基于当前界面编码+动作编码预测下一界面的隐空间表示，无需生成人类可解释的产物
- 动作编码融合类型token、文本语义embedding、与视觉patch共享的位置编码，适配GUI动作的空间语义特性
- 采用change-weighted损失，提升对动作触发的变化区域的训练权重，避免静态UI元素占主导；新增VICReg正则防止表示坍缩、逆动力学辅助损失保留动作相关信息
- 双读出设计：无监督场景用预测与实际表示的余弦差判断跳转是否异常；仅需少量标注训练线性头，即可基于残差方向区分有害/无害异常

### 关键结果
在1.85M真实GUI跳转数据上自监督训练，在自研RSWT-BENCH基准（222对像素完全相同的界面分别对应合法/恶意跳转，单界面检测器AUC强制为0.5）上测试：无监督跳转异常检测AUC达0.987，匹敌Gemini 3.7 Flash、GPT-5.6 Luna等顶级闭源VLM，比生成式GUI世界模型高10个AUC点，延迟仅17ms，快3个数量级；有害/无害异常区分AUC达0.953，远高于prompted VLM的随机水平。

### 核心结论
对于需要机器自动校验预期与现实是否匹配的场景，直接在隐空间做预测比对远比重构出可解释产物再校验高效得多，世界模型除了模拟器、规划器外，还可作为验证器使用
